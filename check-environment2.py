# test.py
import time
import tensorflow as tf

tf.random.set_seed(1)

print("TensorFlow:", tf.__version__)
print("Devices:", tf.config.list_physical_devices())
gpus = tf.config.list_physical_devices("GPU")
print("GPU devices:", gpus)

# 타이밍이 정확히 나오도록 동기 실행 설정 (권장)
tf.config.experimental.enable_op_determinism()
tf.config.experimental.set_synchronous_execution(True)

# 간단한 연산 (행렬곱)으로 CPU vs GPU 시간 비교
SIZE = 4096  # 크면 차이가 더 잘 보임. 느리면 2048로 낮추세요.

def bench(device):
    with tf.device(device):
        a = tf.random.uniform((SIZE, SIZE), dtype=tf.float32)
        b = tf.random.uniform((SIZE, SIZE), dtype=tf.float32)

        # 워밍업 (첫 실행은 그래프 준비 등으로 느릴 수 있음)
        _ = tf.matmul(a, b)

        start = time.perf_counter()
        c = tf.matmul(a, b)
        # 결과를 실제로 사용해 강제 계산
        _ = tf.reduce_sum(c).numpy()
        elapsed = time.perf_counter() - start
        return elapsed

# CPU 벤치마크
cpu_time = bench("/CPU:0")
print(f"CPU matmul: {cpu_time:.3f} sec")

# GPU가 있으면 GPU 벤치마크
if gpus:
    gpu_time = bench("/GPU:0")
    print(f"GPU matmul (Metal): {gpu_time:.3f} sec")
    speedup = cpu_time / gpu_time if gpu_time > 0 else float("inf")
    print(f"Speedup (CPU/GPU): {speedup:.2f}x")
else:
    print("⚠️ GPU가 감지되지 않았습니다. tensorflow-metal 설치/환경 연결을 확인하세요.")