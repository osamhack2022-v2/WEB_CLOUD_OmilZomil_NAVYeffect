

class ImageBox:
    def __init__(self, ai, guardhouse):
        self.ai = ai
        # defualt 값 지정
        self.inspection = {
            'guardhouse': guardhouse,  # 위병소
            'affiliation' : 1,      # 소속
            'rank' : 1,             # 계급
            'name' : "",            # 이름
            'uniform' : 1,          # 복장
        }
        self.parts = {} # 기타 파츠
        # 이미지 관리
        self.main_image = None
        self.parts_image = {}
        self.old_image_count = 0
        # 데이터 갱신 유무
        self.is_update = False
        self.is_best_image = False
        self.parts_update = []  

    
    def get_inspection(self):
        return self.inspection
    
    def get_parts(self):
        return self.parts
    

    def image_process(self, image):
        report = self.ai.detect(org_img=image)
        print(report)

        if report['step'] == 1:
            return "no face"

        if report['step'] == 2:
            return "no milltary"
        
        # 첫 이미지인 경우
        if self.main_image is None:
            # 이미지 저장
            self.main_image = report['boxed_img']
            # 복장 저장
            uniform_name = AI_TABLE['uniform'][report['dress_kind']]
            self.inspection['uniform'] = DB_TABLE['uniform'][uniform_name]
            # 소속 저장
            affiliation = AFFILIATION_TABLE[uniform_name]
            self.inspection['affiliation'] = DB_TABLE['affiliation'][affiliation]
            # parts 저장
            self.parts = {key: False for key in UNIFORM_PARTS[self.inspection['uniform']]} # 유니폼에 따라 파츠 리스트 생성
            self.is_update = True # 정보 갱신

        # 해당 이미지가 잘 나온 이미지인지 판별
        self.best_image(report=report) 
        
        # 각 파츠별 데이터 갱신
        print("Aaaaaaaaaaaaaaaa")
        print(self.parts)
        for part_name, status in report['component'].items():
            if status and self.parts[part_name] == False:
                self.parts[part_name] = True # 양호로 갱신
                self.parts_image[part_name] = report['roi'][part_name]
                self.parts_update.append(part_name) # 업데이트 목록에 추가


        # 각 파츠별 추가 ai 인식
        # 이름 태그가 있으면
        if report['component'].get("name_tag") and self.inspection['name'] == "":
            # 이름 인식
            cached_name = report['component'].get("name_tag")
            self.inspection['name'] = cached_name.replace('cached ', '', 1) #cached  제거

            self.is_update = True        
        # 계급장이 있으면
        if report['component'].get("rank_tag") and self.inspection['rank'] == 1:
            # 계급 인식
            self.inspection['rank'] = DB_TABLE["rank"].get(report['component'].get("rank_tag"))
            self.is_update = True 


    def best_image(self, report):
        if len(report['component']) > self.old_image_count:
            self.main_image = report['boxed_img']
            self.is_best_image = True        

    def find_info(self, component : dict):
        """
        탐지된 파츠로 유니폼과 소속을 찾는 함수
        """
        if "flag" in component.keys():
            self.inspection['uniform'] = "green"
            self.inspection['affiliation'] = "육군"
        elif "muffler" in component.keys():
            self.inspection['uniform'] = "black"
            self.inspection['affiliation'] = "해군"
        elif "muffler" in component.keys():
            self.inspection['uniform'] = "black"
            self.inspection['affiliation'] = "해군"
        else:
            # 일단 해당 복장은 샘당임
            self.inspection['uniform'] = "blue"
            self.inspection['affiliation'] = "해군"
            

