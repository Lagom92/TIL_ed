# Python 아나콘다 가상환경 



- 아나콘다 가상환경 생성

```
conda create --name(-n) 가상환경명 설치할패키지
```



- ex) 파이썬 3.7.3 버전 설치 & test라는 이름으로 가상환경 생성

```
conda create --name test python=3.7.3
```



-  또는

```
conda  create --n test python=3.7.3
```



- 가상환경 활성화, 비활성화

info 명령어를 사용해서 현재 아나콘다의 전체 가상환경 리스트를 조회한다.

가상환경을 만든 후 반드시 activate 명령어로 해당 가상환경을 활성화 후 사용해야 한다.



- 설치 된 가상환경 리스트 확인

```
conda info --envs
```



- 가상환경 활성화( ex) activate test )

```
activate 가상환경명
```



- 가상환경 비활성화( ex) deactivate test )

```
deactivate 가상환경명
```



- 패키지 설치, 패키지 확인

가상 환경 활성화 후 install 명령어를 통해 패키지를 설치할 수 있다.

list 명령어를 통해 해당 프로젝트의 설치된 패키지 리스트를 확인 할 수 있다.



- 패키지 설치 (ex) conda install 패키지명 )

```
conda install simplejson
```



- 패키지 리스트 확인

```
conda list
```



- 가상환경 삭제

생성된 가상환경을 삭제하는 명령어

root 계정으로 활성화 후 삭제하는것을 추천함



- 패키지 삭제 (ex) conda remove --name test --all )

```
conda remove --name 가상환경명 --all
```



- 또는

```
conda remove -n 가상환경명 --all
```



- 캐시 삭제 - 클린

아나콘다는 clean 명령어를 통해 캐시를 삭제할 수 있다.

인덱스 캐시, 잠긴 파일, 사용하지 않는 패키지, 소스 캐시 등을 삭제 할 수 있다.



- 아나콘다 클린

```
conda clean --all
```



- 또는

```
conda clean -a
```







reference

https://niceman.tistory.com/85?category=940952