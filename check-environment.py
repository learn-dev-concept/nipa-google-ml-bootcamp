import tensorflow as tf

print("TensorFlow:", tf.__version__)

# 모든 물리 디바이스 출력
print("All devices:", tf.config.list_physical_devices())

# GPU 디바이스만 출력
gpus = tf.config.list_physical_devices("GPU")
print("GPU devices:", gpus)

# GPU 메모리 증가 방식 설정 여부
if gpus:
    try:
        tf.config.experimental.set_memory_growth(gpus[0], True)
        print("✅ GPU detected and memory growth enabled")
    except RuntimeError as e:
        print("⚠️ GPU detected but memory growth setting failed:", e)
else:
    print("❌ GPU not detected")