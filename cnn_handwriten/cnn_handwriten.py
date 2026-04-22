import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
# ---------- 1. 准备设备（优先使用 GPU） ----------
if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"使用 GPU: {torch.cuda.get_device_name(0)}")
    print(f"CUDA 版本: {torch.version.cuda}")
    print(f"GPU 内存: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")

    # GPU 优化设置
    torch.backends.cudnn.benchmark = True  # 启用 cuDNN 自动调优
    torch.backends.cudnn.deterministic = False  # 允许非确定性算法以提高性能

    # 设置随机种子以确保可重复性
    torch.manual_seed(42)
    torch.cuda.manual_seed(42)
    torch.cuda.manual_seed_all(42)

    print("GPU 优化已启用：cuDNN benchmark 已开启")
else:
    device = torch.device("cpu")
    print("未检测到 GPU，使用 CPU")
    print("建议安装 CUDA 并使用 GPU 以加速训练")

    # CPU 设置随机种子
    torch.manual_seed(42)
# ---------- 2. 数据预处理 ----------
# 将图片转为张量，并归一化到 [-1, 1] 范围（加速训练）
transform = transforms.Compose([
    transforms.ToTensor(),                # 转为 [0,1] 的张量
    transforms.Normalize((0.5,), (0.5,))  # 归一化到 [-1,1]
])
# 下载训练集和测试集（第一次会自动下载）
train_dataset = torchvision.datasets.MNIST(
    root='./data', train=True, download=True, transform=transform
)
test_dataset = torchvision.datasets.MNIST(
    root='./data', train=False, download=True, transform=transform
)
# 数据加载器（分批、打乱）
batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
# ---------- 3. 定义 CNN 模型 ----------
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # 第一个卷积块：输入 1 通道（灰度），输出 16 通道，卷积核 3x3，填充 1（保持尺寸）
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.relu1 = nn.ReLU(inplace=True)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)  # 尺寸减半
        # 第二个卷积块：输入 16 通道，输出 32 通道
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU(inplace=True)
        self.pool2 = nn.MaxPool2d(2, 2)  # 再次减半
        # 第三个卷积块：输入 32 通道，输出 64 通道
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.relu3 = nn.ReLU(inplace=True)
        self.pool3 = nn.MaxPool2d(2, 2)  # 再次减半
        # 经过三次 2x2 池化后，28x28 -> 14x14 -> 7x7 -> 3x3（因为 7/2 向下取整得 3）
        # 所以特征图尺寸为 64 通道 * 3 * 3 = 576
        self.fc1 = nn.Linear(64 * 3 * 3, 128)  # 全连接层
        self.relu_fc = nn.ReLU(inplace=True)
        self.fc2 = nn.Linear(128, 10)          # 输出 10 类（0~9）
    def forward(self, x):
        # x 形状: [batch, 1, 28, 28]
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)   # [batch, 16, 14, 14]
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)   # [batch, 32, 7, 7]
        x = self.conv3(x)
        x = self.relu3(x)
        x = self.pool3(x)   # [batch, 64, 3, 3]
        # 拉平
        x = x.view(x.size(0), -1)  # [batch, 576]
        x = self.fc1(x)
        x = self.relu_fc(x)
        x = self.fc2(x)            # 输出 logits（未归一化）
        return x
# 实例化模型，移到设备
model = SimpleCNN().to(device)
print(model)
# ---------- 4. 定义损失函数和优化器 ----------
criterion = nn.CrossEntropyLoss()        # 交叉熵损失（内部自带 Softmax）
optimizer = optim.Adam(model.parameters(), lr=0.001)
# ---------- 5. 训练一个 epoch 的函数 ----------
def train_one_epoch(epoch_index):
    model.train()          # 设置为训练模式
    running_loss = 0.0
    correct = 0
    total = 0

    # GPU 内存监控
    if device.type == 'cuda':
        torch.cuda.reset_peak_memory_stats()
        start_memory = torch.cuda.memory_allocated() / 1024**2  # MB

    for i, (inputs, labels) in enumerate(train_loader):
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()           # 清零梯度
        outputs = model(inputs)         # 前向传播
        loss = criterion(outputs, labels)  # 计算损失
        loss.backward()                 # 反向传播
        optimizer.step()                # 更新参数
        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        # 每 100 个 batch 打印一次
        if i % 100 == 99:
            print(f"Epoch {epoch_index+1}, Batch {i+1}: loss = {running_loss/100:.4f}")
            if device.type == 'cuda':
                current_memory = torch.cuda.memory_allocated() / 1024**2
                peak_memory = torch.cuda.max_memory_allocated() / 1024**2
                print(f"GPU 内存使用: 当前 {current_memory:.1f}MB, 峰值 {peak_memory:.1f}MB")
            running_loss = 0.0
    epoch_acc = 100 * correct / total

    # 显示 epoch 结束时的 GPU 内存信息
    if device.type == 'cuda':
        final_memory = torch.cuda.memory_allocated() / 1024**2
        peak_memory = torch.cuda.max_memory_allocated() / 1024**2
        print(f"Epoch {epoch_index+1} GPU 内存: 最终 {final_memory:.1f}MB, 峰值 {peak_memory:.1f}MB")

    return epoch_acc
# ---------- 6. 评估函数 ----------
def evaluate():
    model.eval()           # 设置为评估模式
    correct = 0
    total = 0
    with torch.no_grad():  # 不计算梯度，节省内存
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return 100 * correct / total
# ---------- 7. 训练循环 ----------
num_epochs = 10
train_accs = []
test_accs = []
for epoch in range(num_epochs):
    train_acc = train_one_epoch(epoch)
    test_acc = evaluate()
    train_accs.append(train_acc)
    test_accs.append(test_acc)
    print(f"Epoch {epoch+1} 结束：训练准确率 = {train_acc:.2f}%, 测试准确率 = {test_acc:.2f}%")
    print("-" * 50)
print("训练完成！")
# ---------- 8. 画出训练曲线 ----------
plt.figure(figsize=(10, 5))
plt.plot(range(1, num_epochs+1), train_accs, label='训练准确率', marker='o')
plt.plot(range(1, num_epochs+1), test_accs, label='测试准确率', marker='s')
plt.xlabel('训练轮数')
plt.ylabel('准确率 (%)')
plt.title('CNN 在 MNIST 上的学习曲线')
plt.legend()
plt.grid(True)
plt.show()
# ---------- 9. 随机看几个预测结果 ----------
model.eval()
images, labels = next(iter(test_loader))
images, labels = images.to(device), labels.to(device)
outputs = model(images)
_, preds = torch.max(outputs, 1)
# 显示前 10 张
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
axes = axes.ravel()
for i in range(15):
    img = images[i].cpu().squeeze().numpy()  # 转为 28x28 数组
    axes[i].imshow(img, cmap='gray')
    axes[i].set_title(f'真:{labels[i].item()} 预:{preds[i].item()}')
    axes[i].axis('off')
plt.tight_layout()
plt.show()