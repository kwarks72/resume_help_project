Resume Helper

AI가 자기소개서를 분석하고 첨삭해주는 CLI 프로그램입니다.

Features
자기소개서 첨삭
지원동기 분석
경험 분석
STAR 구조 기반 피드백
Installation
uv pip install python-dotenv openai anthropic
Run
uv run python resume_helper.py
Commands
Command	Description
/help	도움말
/quit	프로그램 종료
Project Structure
resume-helper/
├── resume_helper.py        # CLI 실행
├── resume_agents.py        # AI 첨삭 로직
├── styles.py               # 출력 스타일
├── README.md
└── week8_retrospective.md
Notes
API 키는 .env 파일에 저장합니다.
.env 파일은 GitHub에 업로드하지 않습니다.
개인정보 입력은 권장하지 않습니다.
