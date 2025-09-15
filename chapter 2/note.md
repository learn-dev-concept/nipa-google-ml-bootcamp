


DNN에서의 레이어 종류

CNN에서의 레이어 종류

Feature Extraction --> 파라미터 계산법
- 필터 크기가 3x3 이면 가중치가 9개
- 이전 뉴런 32x3x3x64 + 64


영상처리에서는 합성곱이라기보다 필터처리 한다 라고 표현함 주로.
DNN에서 가중치는 숫자 1개에 1개, CNN에서는 숫자 1개에 필터 크기만큼의 숫자
필터는 



합성곱 레이어에서 가중치는 배열로 지정 + 배열은 홀수x홀수 형태여야 함.

padding='same' --> zero padding



shape 함수 관련 정리해~~
```python
import numpy as np

x = np.zeros((28, 28, 1))
print(x.shape)
print(x)
print(x[0])
```
