# import torch
# x = torch.rand(5, 3)
# print(x)
import torch
import sys
import platform

def verify_pytorch_installation():
    print("=" * 60)
    print("PyTorch 安装验证")
    print("=" * 60)
    
    # 系统信息
    print(f"操作系统: {platform.system()} {platform.release()}")
    print(f"Python版本: {sys.version}")
    
    # PyTorch 基本信息
    try:
        print(f"PyTorch版本: {torch.__version__}")
        print(f"PyTorch路径: {torch.__file__}")
        print("✓ PyTorch 导入成功!")
    except ImportError as e:
        print(f"✗ PyTorch 导入失败: {e}")
        return False
    
    # CUDA 支持
    cuda_available = torch.cuda.is_available()
    print(f"CUDA可用: {cuda_available}")
    
    if cuda_available:
        print(f"CUDA版本: {torch.version.cuda}")
        print(f"GPU数量: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("  - 使用CPU模式")
    
    # 基本功能测试
    print("\n基本功能测试:")
    try:
        # 张量创建
        x = torch.tensor([1, 2, 3])
        y = torch.tensor([4, 5, 6])
        z = x + y
        print(f"✓ 张量运算: {x} + {y} = {z}")
        
        # 自动求导
        w = torch.tensor(2.0, requires_grad=True)
        loss = w ** 2
        loss.backward()
        print(f"✓ 自动求导: d(loss)/dw = {w.grad}")
        
        # 矩阵乘法
        A = torch.randn(2, 3)
        B = torch.randn(3, 2)
        C = torch.mm(A, B)
        print(f"✓ 矩阵乘法: {A.shape} × {B.shape} = {C.shape}")
        
        print("\n🎉 所有测试通过! PyTorch 安装成功!")
        
    except Exception as e:
        print(f"✗ 功能测试失败: {e}")
        return False
    
    print("=" * 60)
    return True

if __name__ == "__main__":
    verify_pytorch_installation()                                  
   
      