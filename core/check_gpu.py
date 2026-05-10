import sys


def check_hardware():
    """
    Detect available Intel hardware acceleration.
    Priority: OpenVINO GPU (OpenCL) > OpenVINO CPU > PyTorch CPU fallback.
    """
    print("=" * 60)
    print("  Hardware Acceleration Check")
    print("=" * 60)

    # --- Step 1: Check OpenVINO ---
    try:
        from openvino import Core
        core = Core()
        available_devices = core.available_devices

        print(f"\n✅ OpenVINO detected!")
        print(f"   Version: {core.get_versions('CPU')['CPU'].build_number}")
        print(f"   Available devices: {', '.join(available_devices)}")

        if "GPU" in available_devices:
            gpu_name = core.get_property("GPU", "FULL_DEVICE_NAME")
            print(f"\n🎉 Intel iGPU found: {gpu_name}")
            print(f"   Backend: OpenCL (not Level Zero)")
            print(f"   Supported modes: CPU, GPU, MULTI:CPU,GPU, AUTO")
            print(f"\n   Recommended config for LLAA:")
            print(f"     • LLM inference (Ollama) → CPU")
            print(f"     • Embeddings (ChromaDB)  → GPU via OpenVINO")
            print(f"     • Combined workloads     → AUTO or MULTI:CPU,GPU")
        else:
            print(f"\n⚠️  No GPU device in OpenVINO (OpenCL driver may be missing).")
            print(f"   CPU-optimized inference is still available.")
            _suggest_opencl_fix()

    except ImportError:
        print("\n⚠️  OpenVINO not installed.")
        print("   Install with: pip install openvino optimum-intel")

    # --- Step 2: Check PyTorch (for Ollama/general use) ---
    print("\n" + "-" * 60)
    try:
        import torch
        print(f"\n✅ PyTorch {torch.__version__} available (CPU backend)")
    except ImportError:
        print("\n⚠️  PyTorch not installed.")

    # --- Step 3: System summary ---
    print("\n" + "=" * 60)
    print("  Summary")
    print("=" * 60)
    _print_system_info()


def _suggest_opencl_fix():
    """Suggest how to enable OpenCL for Intel iGPU on Linux."""
    print("\n   To enable GPU support, install Intel OpenCL runtime:")
    print("   sudo apt install intel-opencl-icd")
    print("   Then re-run this check.")


def _print_system_info():
    """Print system info relevant to AI inference."""
    import platform
    try:
        import psutil
        ram_gb = psutil.virtual_memory().total / (1024 ** 3)
        cpu_count = psutil.cpu_count(logical=True)
        print(f"\n   OS:       {platform.system()} {platform.release()}")
        print(f"   Python:   {platform.python_version()}")
        print(f"   CPU:      {cpu_count} logical cores")
        print(f"   RAM:      {ram_gb:.1f} GB total")
        print(f"   Note:     iGPU shares system RAM (no dedicated VRAM)")
    except ImportError:
        print(f"\n   OS:       {platform.system()} {platform.release()}")
        print(f"   Python:   {platform.python_version()}")


if __name__ == "__main__":
    check_hardware()
