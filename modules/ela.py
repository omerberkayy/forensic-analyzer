from core.common import AnalysisResult, verdict_from_score

def analyze(file_bytes: bytes, filename: str) -> AnalysisResult:
    # TODO Paket 2: gerçek ELA
    score = 0.5
    return AnalysisResult(
        method="ELA", score=score, verdict=verdict_from_score(score),
        findings=["(STUB) Henüz uygulanmadı"], media_type="image")