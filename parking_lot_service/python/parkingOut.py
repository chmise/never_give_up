import cv2 #opencv 모듈
import numpy as np
import pytesseract #테서렉트 모듈
from datetime import datetime
import time
import pymysql #mysql 모듈
import serial #시리얼통신 모듈
import pygame

# 할때 변수 통일 포트 통일 등등

# 주차자리 유무 판단해서 있으면 아래 코드 진행

# opencv로 노트북 웹캠으로 찍어서 저장 가능한지 확인

# 카메라로 사진을 찍어graysacle로 변환

# 가우시안블러를 사용해 노이즈를 줄인 후 이미지의 이진화 수행

# 이미지에서 컨투어 찾기

# 컨투어를 감싸는 사각형을 구하고 좌표 정보 저장

# 번호판인 것 같은 컨투어 추려내기

# 남은 컨투어 중에서 기준을 강화해 추려내기
# 1. 컨투어의 가로, 세로가 모두 동일하거나 비슷한지
# 2. 컨투어 사이의 간격은 일정한지
# 3. 최소 3개 이상의 컨투어가 인접해 있는지

# 후보군의 컨투어 개수가 맞는지 판단

# 컨투어 X방향으로 정렬

# 기울어진 각도 구해도 똑바로 회전

# 테서렉트를 통해 이미지를 읽음

# 번호판 판별식
# 1. 숫자만 남기고 특수문자 삭제
# 2. 결과 중 가장 긴게 번호판
# 3. 번호판 내용보다 길 경우 숫자3 한글1 숫자4의 내용만 남김

# 입차시간과 현재시간의 차로 요금 계산 로직

# 차단기 퍼미션을 아두이노에 전송
