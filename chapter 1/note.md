
## Data-Set 종류

### train
- 학습에 사용되는 데이터

### val
- 매 이폭(epochs)마다 학습된 몯레을 평가하기 위한 데이터셋, val이 없을 경우 train으로 매 이폭마다 평가

### test
- 학습이 완료된 모델의 평가를 위한 데이터셋

```
[참고] 학습 중 모델을 평가할 때의 데이터 셋
- accuracy, loss --> train
- val_accuracy, val_loss --> val
```



1. 원핫 인코딩이란
- 출력층에서 나온 값을 정답 데이터와 어떻게 비교하는가?

2. 다중 분류 문제에서 출력층에 softmax 활성화 함수를 사용하는 이유