# core/common.py
from dataclasses import dataclass, field, asdict
from typing import Any, List, Dict, Optional
from enum import Enum


class Verdict(str, Enum):
    AUTHENTIC = "authentic"       # Gerçek görünüyor
    SUSPICIOUS = "suspicious"     # Şüpheli
    MANIPULATED = "manipulated"   # Manipüle edilmiş / AI üretimi
    INCONCLUSIVE = "inconclusive" # Sonuç çıkarılamadı
    ERROR = "error"               # Analiz hatası


def verdict_from_score(score: float,
                       low: float = 0.35,
                       high: float = 0.65) -> Verdict:
    """score: 0 = kesin gerçek, 1 = kesin sahte."""
    if score < low:
        return Verdict.AUTHENTIC
    if score < high:
        return Verdict.SUSPICIOUS
    return Verdict.MANIPULATED


@dataclass
class AnalysisResult:
    method: str                          # "ELA", "EXIF", "Image AI", "Audio AI"
    score: float                         # 0.0 - 1.0 (1 = sahte olma olasılığı)
    verdict: Verdict
    findings: List[str] = field(default_factory=list)   # insan okuyabilir bulgular
    figures: Dict[str, Any] = field(default_factory=dict)  # {"ELA Farkı": PIL.Image, ...}
    details: Dict[str, Any] = field(default_factory=dict)  # ham teknik veri
    media_type: str = "image"            # "image" | "audio"
    elapsed_sec: Optional[float] = None

    def __post_init__(self):
        self.score = max(0.0, min(1.0, float(self.score)))

    def to_dict(self, include_figures: bool = False) -> dict:
        d = asdict(self)
        d["verdict"] = self.verdict.value
        if not include_figures:
            d["figures"] = list(self.figures.keys())
        return d

    @classmethod
    def error(cls, method: str, message: str, media_type="image"):
        return cls(method=method, score=0.0, verdict=Verdict.ERROR,
                   findings=[f"Analiz başarısız: {message}"],
                   media_type=media_type)