# WEB_CLOUD_OmilJomil_NAVYeffect
![1  타이틀](https://user-images.githubusercontent.com/59905641/198581773-d1f0b268-8a9c-46b9-8ba9-909eb4a1a172.png)
# :sunglasses: 오밀조밀 : 외적 군기 디텍팅 솔루션 :whale:

### 기지 정문에 카메라를 설치, 외적 군기 불량 여부를 판단해 부대 관리자 및 병들이 볼 수 있는 체계에 제공한다.


## :pencil: INDEX
<details open="open">
  <ol>
    <li><a href="#intro"> ᐅ 프로젝트 소개 (Intro)</a></li>
    <li><a href="#features"> ᐅ 기능 설명 및 사용법 (Features)</a></li>
      <ol>
        <li><a href="Structures">  ᐅ 구조 설명 (Structures)</a></li>
        <li><a href="ux/ui">  ᐅ UX / UI</a></li>
      </ol>
    <li><a href="#pre-required"> ᐅ 컴퓨터 구성 / 필수 조건 안내 (Pre-required)</a></li>
    <li><a href="#technique"> ᐅ 기술 스택 (Technique used)</a></li>
    <li><a href="#install"> ᐅ 설치 안내 (How to download)</a></li>
    <li><a href="#team"> ᐅ 팀원 정보 (Meet the team)</a></li>
    <li><a href="#copyright"> ᐅ 저작권 및 사용권 정보 (Copyright and License)</a></li>
    <li><a href="#appendex"> ᐅ 부록 (Appendex)</a></li>
  </ol>
</details>

# sections

<h2 id="intro"> :grey_question: 프로젝트 소개 (Intro)</h2>

> + 카메라를 설치해, AI가 군 기지 출입시 두발 및 복장 불량 여부를 인식한다.
>    + 대시보드에 부대별, 전군 실시간 데이터를 올려 통계직인 여러 인사이트를 게재한다.
>    + 각 부대 담당 간부는 접근 가능한 계정을 부여받아 이를 통해 확인할 수 있다.
>    + 기지 내 사병들 또한 외적 군기 위반 요소들을 확인해 스스로 점검할 수 있다.

### 개요
군기는 군대의 기율이며 생명과 같기에 항상 엄정한 군기를 세워야 합니다. 또한 군기는 곧 사기이며, 이를 가장 잘 나타내는 부분이 외적 군기와 제식 훈련입니다. 다만 제식은 특별한 상황이 아니면 평상시에 보여줄 수 있는 부분이 아니기 때문에 평시에 외적 군기 확립을 중시 여길 수밖에 없습니다.

그러나 두발 상태 불량부터 시작해 명찰, 계급장, 모자까지,,, 

 *외적 군기 위반 요소는 매우 다양합니다.*

우리 **NAVY효과의 "오밀조밀"은 이러한 사례들을 수집해 관리자, 일반 사병, 군사 경찰 할 것 없이 기지 내 장병들에게 편의와 인사이트를 제공하는 솔루션**이 될 것입니다.

<h2 id="features"> :mag: 기능 설명 및 프로젝트 사용법 (Features)</h2>

<h3 id="Structures"> :gear: 구조 설명 (Structures)</h3>


![5  프로젝트 상세  구조도](https://user-images.githubusercontent.com/59905641/198606538-941de90b-358c-4b2b-b2dd-bdd42d771104.png)
> 프로젝트 상세 구조도
 + 저희 프로젝트는 크게 *세 가지의 컨테이너로 구성*되어 있습니다.  
각각 카메라로 찍은 사진을 가져오고 저장해 모듈화된 AI로 판별하는 **WebRTC Backend 컨테이너**, 그렇게 만들어진 DB를 담은 **DB 컨테이너**, 그리고 그 안의 데이터를 파싱해서 저희 오밀-조밀 웹 서비스에 대시보드나 통계 자료를 볼 수 있게 하는 **Omil-Zomil Backend 컨테이너**입니다.  
따라서 *메인 리드미 파일 말고도 WebRTC 리드미 파일, 오밀-조밀 리드미 파일 또한 존재*하니 필독 부탁드립니다.  

<h3 id="ux/ui"> :computer: UX / UI</h3>


> 프로젝트 핵심 기능들입니다. 상세 설명 및 그 외 다양한 페이지 설명은 부록의 Omil-Zomoli readme.md를 필히 참고하여 주시기 바랍니다.

  + #### 대시보드 : 부대별 대시보드입니다. 실시간으로 출입자 정보가 리스트업되며, 각 요소 별 불량 비율이나 월간 양호 빈도 등을 제공합니다.
![대시보드](https://user-images.githubusercontent.com/59905641/198835988-dbbb25c4-9aa0-4412-b985-21f7232fc773.gif)

 + #### 실시간 감지 현황 : 부대 인원 조회 페이지입니다. 자세히 보기 클릭 시 상세 정보 팝업창이 뜹니다.
![실시간 감지 현황](https://user-images.githubusercontent.com/59905641/198836560-3cce9488-ff6e-48e0-a826-6417643aae68.gif)

 + #### 전군 통계 : 전군 통계 대시보드입니다. 각군별, 시간대별, 요소 별 불량 여부 등의 통계적 데이터로 넓은 범위에서의 추이를 볼 수 있습니다. 사진변경해야!!!
![전군통계](https://user-images.githubusercontent.com/59905641/194753907-dc546fd1-81f1-4e42-b2f8-f0d0efea910c.png)

 + #### 랭킹 페이지 : 위반 요소별 리스트업 및 상위 부대 꾸미기 기능으로 상승 욕구를 돋울 수 있습니다.
![랭킹 페이지](https://user-images.githubusercontent.com/59905641/198837991-9da0682c-e55d-401c-b051-72f589e37e3b.png)

![17  프로젝트 상세  사용자기능](https://user-images.githubusercontent.com/59905641/198816658-e15f9c3f-22f0-487f-9f85-4927ab828f76.png)

![22  깃허브](https://user-images.githubusercontent.com/59905641/198816675-e67b4f42-93a2-436c-9d28-be39604e000e.png)
![18  프로젝트 상세  프로필 수정2](https://user-images.githubusercontent.com/59905641/198816687-9e13d999-afef-440a-8c59-3a4bc35d6883.jpg)
 
 + 수정/관리 페이지입니다. 루트 관리자, 일반 관리자(부대 관리자)에게 서로 다른 페이지를 보여줍니다. 프로필 등을 수정하는 기능 및 회원 탈퇴가 가능합니다.
![루트관리자-프로필수정](https://user-images.githubusercontent.com/59905641/194754473-8e47d034-b061-4ad2-b1fd-14480a3874fb.png)
![일반관리자-프로필수정](https://user-images.githubusercontent.com/59905641/194754528-4380629c-4117-4296-a9e0-60df82ff5704.png)

<h2 id="pre-required"> :dash: 컴퓨터 구성 / 필수 조건 안내 (Pre-required)</h2>

> WebRTC 사용 덕에 타 플러그인 필요 없음. 웹 브라우저로 바로 접속 가능. 한 줄 설명하고 가능한 브라우저 종류, 버전 등 적기(개발진문의)
 + ECMAScript 6 지원 브라우저 사용
 + 권장: Google Chrome 버전 77 이상
 + Internet Explorer 미사용 추천 등

<h2 id="technique"> :technologist: 기술 스택 (Technique used)</h>

### Back end
 + <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
 + <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white">

### DB(back-end)
 + <img src="https://img.shields.io/badge/MySQL-#4479A1?style=for-the-badge&logo=MySQL&logoColor=white">

### AI(back-end)
 + lib : <img src="https://img.shields.io/badge/TensolFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white"> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=OpenCV&logoColor=white">

 + model : <img src="https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=YOLO&logoColor=white"> v4, swit-transformer, HED(Holistically-Nested Edge Dataset), MobileNet
 + dataset : MS-COCO, Pascal VOC Dataset Mirror, CelebAMask-HQ, Figaro-1k, Lft

### Front end
 + <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=Vue.js&logoColor=white">
 + <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white">
------------------------------------------------------------------------------------------------------------------------------------------
![21  사용기술및오픈소스](https://user-images.githubusercontent.com/59905641/198816673-be370969-93a8-4f35-952e-144f5394db3d.png)
<h2 id="install"> :arrow_down: 설치 안내 (How to download)</h2>

**생활반 가서 오밀조밀 주소로 변경**
<h2 id="team"> :kissing_heart: 팀원 정보 (Meet the team)</h2>

> 팀 NAVY효과

| Name | Role | Contect |   
|:---:|:---:|:---:| 
|조남훈| 팀장, 기획자 | lovin6109@gmail.com |   
|조준영| AI 개발자, 웹 디자이너 | joon0zo1022@gmail.com |
|정의철| 백엔드 개발자 | com.dos.m0nk3y@gmail.com |
|김대원| DevOps 담당자 | kdwkd0078@gmail.com |   
|허태량| 프론트 엔드 개발자 | cake0702@naver.com |   
|김민섭| 프론트 엔드 개발자 | tjqtjq0516@gmail.com |

<h2 id="copyright"> :books: 저작권 및 사용권 정보 (Copyright & License)</h2>

 + MIT
This project is licensed under the terms of the MIT license.


<h2 id="appendex"> :card_index: 부록 (Appendex)</h2>

> 개발 문서

리드미들 링크는 머지한 다음에 main 브랜치로 다시 링크 걸어야 할 것!

+ [WebRTC readme](https://github.com/osamhack2022-v2/WEB_CLOUD_OmilZomil_NAVYeffect/blob/document/webrtc/Readme.md)
+ [Omil-Zomil readme](https://github.com/osamhack2022-v2/WEB_CLOUD_OmilZomil_NAVYeffect/blob/document/omilzomil/Readme.md)
+ <a href="https://www.figma.com/file/SWq5gdsKhBOHZJrDL5Qjr8/%EC%98%A4%EB%B0%80%EC%A1%B0%EB%B0%80-(NAVY%ED%9A%A8%EA%B3%BC)?node-id=1199%3A4300"><img src="https://img.shields.io/badge/Figma-#F24E1E?style=for-the-badge&logo=Figma&logoColor=white"></a>
+ Wireframes 모음집(Wiki 참고)
+ 멘토링 준비-결과 자료집(Wiki 참고) 아직
+ 발표자료 ppt(Wiki 참고) 아직
