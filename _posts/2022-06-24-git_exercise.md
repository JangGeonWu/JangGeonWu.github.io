---
layout: single
title:  "github의 기본 정리"
---

# github에 익숙해지기 위해서
github에서 사용하는 문법들을 정리하기 위한 페이지이다.

git init (시작으로 .git/을 생성한다. )

git add . (현재 디렉토리에 있는 모든 파일들을 히스토리에 기록한다.)
git status (현재 히스토리에 기록된 내용을 요약하여 볼 수 있다. )
git commit -m "commit name" (현재 히스토리를 'commit name'으로 저장한다.)

git remote -v : 현재 연결고리를 확인한다.
git push origin `branch_name` : 원하는 branch에 push를 진행한다

git checkout `branch_name` : 원하는 branch로 변경한다
git checkout -b `branch_name` : 원하는 branch를 생성하면서 변경한다

git branch : 현재 branch 정보를 확인한다

git clone ~~~ `folder_name` : (저장하고픈 경로에서) `folder_name`이라는 곳에 github 파일들을 내려받는다

### 새로운 버전 pull하기 위해서는
1. git add ., git commit -m "abcd"를 수행한다
2. git pull origin `branch_name` : 해당 branch로부터 동기화

### master가 아닌 branch로 push를 했을 경우
pull request = (master branch로의)pull 요청
master는 둘 중 하나를 수행한다:
* 수락: merge pull request
* 거절: review changes
