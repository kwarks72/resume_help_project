Resume Helper
프로젝트 소개

자소서를 입력하면 AI가 첨삭해주는 CLI 프로그램입니다.

기능:

자소서 첨삭
지원동기 및 경험 분석
STAR 구조 기반 피드백
실행 방법

패키지 설치

uv pip install python-dotenv openai anthropic

실행

uv run python resume_helper.py
사용 방법

프로그램 실행 후 자소서를 입력합니다.

명령어

/help

도움말 출력

/quit

프로그램 종료

파일 구조
resume-helper/
├── resume_helper.py
├── styles.py
├── resume_agents.py
├── README.md
└── week8_retrospective.md
주의 사항
API 키는 .env 파일에 저장합니다.
.env는 GitHub에 업로드하지 않습니다.
개인정보는 입력하지 않는 것을 권장합니다.