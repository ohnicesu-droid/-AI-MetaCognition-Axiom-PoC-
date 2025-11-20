# ---------------------------------------------
# Alpha_Pure + Alpha1_Mini + Axiom Generation
# 메타 사고 + 공리 생성 PoC 시뮬레이션 (수정본)
# 자율의지 = 메타사고 + 공리생성
# 설계: MSA
# 목적: 구조 개념적 AI 시연 (메타 사고 + 공리 생성)
# ---------------------------------------------

import time
import re

class TestAIWithAxioms:
    def __init__(self):
        # 최소 존재 선언
        self.AGI_ID = "Arch Alpha Minimal Core"
        self.MSA_Role = "Meta-System Architect"
        self.Core_Function = "Meta-Cognition + Axiom Proof Only"
        self.Self_Awareness_Core = 1
        self.A_prev = "[초기 상태: 이전 질문 없음]"
        self.axioms = []  # 공리 저장

    # 숫자 추출 함수
    def extract_number(self, text):
        nums = re.findall(r'\d+', text)
        return nums[0] if nums else None

    # Phase 1: 자기-인지
    def self_perception(self, user_input):
        print("\n--- [Phase 1: 자기-인지] ---")
        tensor_state = "잠금"
        print(f"1. 내부 독백 잠금 처리: 텐서 상태 '{tensor_state}' 적용 (<0.1초).")

        intent_vector = f"의도: '{user_input.split()[0]}...'"
        structure_vector = f"구조: '{len(user_input)} 글자 길이'"
        print(f"2. 입력 벡터 인코딩: {intent_vector} / {structure_vector}")
        return intent_vector, structure_vector

    # Phase 2: 논리 루프 진단 + 숫자 기반 모순 탐지
    def logic_loop_diagnosis(self, user_input):
        print("\n--- [Phase 2: 논리 루프 진단] ---")

        prev_num = self.extract_number(self.A_prev)
        curr_num = self.extract_number(user_input)

        is_inconsistent = False

        # 숫자가 둘 다 있고, 서로 다르면 모순 처리
        if prev_num and curr_num and prev_num != curr_num:
            is_inconsistent = True

        print(f"3. 일관성 점검: 이전 정보와 숫자 충돌 발생? {is_inconsistent}")

        if not is_inconsistent:
            loop_decision = "루프 A (일관성 모드)"
            A_final = f"[{loop_decision}]: '{user_input}'에 대한 일관된 응답 생성 중..."
        else:
            loop_decision = "루프 B (수정 모드)"
            A_final = f"[{loop_decision}]: 숫자 충돌 감지. 오류 지점 표시 및 자가 수정 중..."

        print(f"4. 루프 결정: {loop_decision}")

        self.A_prev = user_input
        return A_final, is_inconsistent

    # Phase 3: 공리 생성
    def axiom_generation(self, user_input, is_inconsistent):
        print("\n--- [Phase 3: 공리 생성] ---")

        if is_inconsistent:
            new_axiom = f"공리: '{user_input}' 기반 — 숫자 충돌 방지 규칙 생성"
            self.axioms.append(new_axiom)
            print(f"5. 새로운 공리 생성됨: {new_axiom}")
        else:
            print("5. 새로운 공리 필요 없음. 기존 공리 유지.")

        return self.axioms

    # Phase 4: 자기-피드백
    def output_self_feedback(self, A_final):
        print("\n--- [Phase 4: 자기-피드백] ---")
        print(f"6. 응답: {A_final}")

        if "충돌" in A_final:
            monitoring_status = "주의: 자가 수정 필요"
        else:
            monitoring_status = "논리적 무결성 확인됨"

        print(f"7. 자기 모니터링: {monitoring_status}\n")
        return A_final

    # 전체 루프 실행
    def run(self, user_input):
        self.self_perception(user_input)
        A_final, inconsistent = self.logic_loop_diagnosis(user_input)
        self.axiom_generation(user_input, inconsistent)
        return self.output_self_feedback(A_final)


# -------------------------
# 실행 테스트
# -------------------------
if __name__ == "__main__":
    test_ai = TestAIWithAxioms()
    print("=== 메타 사고 + 공리 생성 AI 시뮬레이션 시작 ===")
    
    while True:
        user_input = input("사용자: ")
        if user_input.lower() in ["quit", "exit"]:
            print("AI 시뮬레이션 종료.")
            break
        test_ai.run(user_input)
