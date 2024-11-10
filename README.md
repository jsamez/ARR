# 레시피 추천 프로그램: ARR

## 팀 정보
- **팀명:** ARR
- **지도 교수님:** 조용호 교수님
- **팀원:**
  - 김예찬 (193409): 카메라를 이용한 데이터 처리 및 코드 작성
  - 원준혁 (193423): 프로젝트 총괄 및 운영, 필요 물품 구입, 인공지능 딥러닝 구현
  - 장성민 (193436): 자료조사, 데이터베이스 및 알고리즘 코드 작성
  - 최진호 (193451): 자료조사 보조, 데이터베이스 및 구현 코드 작성

---

## 목차
1. 팀원별 역할
2. 개발일정
3. 목적계통도
4. 기능블록도 및 작품의 요약 설명
5. 설계 제한 요소
6. 사용 소프트웨어 및 하드웨어 목록과 설명
7. 작품 상세 설명 및 알고리즘
8. 자체 평가 및 소감
9. 참고자료 목록
10. 소스코드
11. 작품사진

---

## 1. 팀원별 역할
| 팀원     | 역할                              |
|----------|-----------------------------------|
| 김예찬    | 카메라를 이용한 데이터 처리 및 코드 작성 |
| 원준혁    | 프로젝트 총괄 및 운영, 필요 물품 구입, 딥러닝 구현 |
| 장성민    | 자료조사, 데이터베이스 및 알고리즘 코드 작성 |
| 최진호    | 자료조사 보조, 데이터베이스 및 구현 코드 작성 |

---

## 2. 개발일정
![개발 일정](images/images000001)

---

## 3. 목적계통도
![목적 계통도](images/images000002)

---

## 4. 기능블록도 및 작품의 요약 설명
1. 노트북 카메라가 음식 재료를 인식합니다.
2. 인식된 음식 재료 데이터를 배열로 받습니다.
3. 데이터베이스와 비교하여 일치하는 레시피와 추가 재료가 필요한 레시피를 추천합니다.
   - 추가 재료가 필요한 경우 필요한 재료들을 보여줍니다.
4. 최종적으로 선택된 레시피를 텍스트로 보여줍니다.

![기능 블록도](images/images000003)

---

## 5. 설계 제한 요소
| 제한 요소   | 설계 사양                                                          |
|------------|---------------------------------------------------------------------|
| 경제성     | 카메라만을 이용하여 비용 절감을 목표로 합니다.                       |
| 신뢰성     | 재료를 정확히 인식하여 사용자에게 적절한 레시피를 추천해야 합니다.     |
| 사회적 영향| 음식물 쓰레기 배출을 줄이는 것을 목표로 설계합니다.                   |
| 기능성     | 사용자가 쉽게 사용할 수 있도록 설계하였습니다.                      |

![설계 제한 요소](image/image000004)

---

## 6. 사용 소프트웨어 및 하드웨어 목록
### 소프트웨어
- **YOLO** - 이미지 인식
- **OpenCV** - 이미지 처리
- **Pycharm** - 코드 작성 환경
- **BeautifulSoup** - 웹 스크래핑
- **Excel** - 데이터 관리

### 하드웨어
- **노트북**
- **카메라**

![소프트웨어 및 하드웨어 목록](images/images000005)

---

## 7. 작품의 상세 설명 및 알고리즘
1. 각종 레시피들을 모은 데이터베이스를 구축합니다.
2. 노트북 카메라를 이용하여 음식 재료를 객체 인식합니다.
3. 객체 인식된 음식 재료를 배열로 저장하여 데이터베이스와 비교 후 일치하는 레시피를 출력합니다.
4. 사용자가 원하는 레시피를 선택할 수 있으며, 해당 레시피를 GUI로 출력합니다.

![작품 상세 설명](images/images000006)

---

## 8. 자체 평가 및 소감
- **팀원별 소감**  
  - **김예찬:** YOLO v8 커스텀 학습에 대한 이해를 높였으며, 이를 실생활에 적용해보는 좋은 경험이었습니다.
  - **원준혁:** 딥러닝 기술을 실생활 문제 해결에 적용하는 방법을 체험했습니다.
  - **장성민:** 객체 인식 학습자료 제작 과정을 이해하는 유익한 프로젝트였습니다.
  - **최진호:** 실시간 음식 재료 감지와 추천 요리 제공 과정이 흥미로웠으며, 추가 학습을 통한 인식 정확도 향상을 희망합니다.

![자체 평가](images/images000007)

---

## 9. 참고자료 목록
- [크롤링 하는 방법](https://otugi.tistory.com/393)
- [YOLO v5 설치 및 사용법](https://jeo96.tistory.com/entry/YOLOv5-설치-Pycharm)
- [딥러닝 프레임워크 GPU 사용법](https://jeo96.tistory.com/entry/Pytorch-CUDA-cuDNN-설치-windows-10)
- [텐서플로우 객체인식 방법](https://pseong.tistory.com/16)
- [라벨미를 통한 학습 데이터 제작 방법](https://made-by-kyu.tistory.com/entry/OpenCV-YOLOv8-커스텀-학습-데이터-만들기)

---

## 10. 소스코드
소스코드는 음식 재료를 인식하고 레시피를 추천하는 기능을 포함하고 있으며, 자세한 내용은 본 보고서의 소스코드 섹션에서 확인할 수 있습니다.

---

## 11. 작품사진
![작품 사진](images/images000008)
