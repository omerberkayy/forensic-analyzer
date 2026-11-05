# forensic-analyzer
Fotoğraf ve ses delillerinde sahtecilik tespit sistemi (ELA, EXIF, AI)

score: 0 = gerçek, 1 = sahte (tüm modüllerde aynı yön)
figures: değerler PIL.Image, matplotlib.figure.Figure veya numpy dizisi olabilir
Her analiz fonksiyonu hata fırlatmaz, AnalysisResult.error(...) döndürür
Fonksiyon imzası: analyze(file_bytes: bytes, filename: str) -> AnalysisResult