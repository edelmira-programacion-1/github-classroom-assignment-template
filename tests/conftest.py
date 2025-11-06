import json, pytest

def pytest_configure(config):
    config._results = []
    config.addinivalue_line("markers", "points(n): puntaje del test")

# --- Hook 2: Reporte de cada test ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when != "call":
        return
    marker = item.get_closest_marker("points")
    points = float(marker.args[0]) if marker and marker.args else 1.0

    item.config._results.append({
        "test": item.nodeid,
        "resultado": rep.outcome,
        "puntaje": points,
    })

def pytest_sessionfinish(session):
    results = session.config._results
    if not results:
        print("\nNo se encontraron resultados de tests para calificar.")
        return

    max_score = sum(r["puntaje"] for r in results)
    score = sum(r["puntaje"] for r in results if r["resultado"] == "passed")
    percentage = (score / max_score * 100.0) if max_score > 0 else 0.0
    payload = {"Puntaje": score, "Puntaje máximo": max_score, "Calificación": percentage, "Resultados": results}

    with open("calificacion.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    for i, r in enumerate(results, 1):
        status = "PASSED" if r["resultado"] == "passed" else "NOT PASSED"
        print(f"test {i}: {status}")

    print(f"\n=== CALIFICACION: {score}/{max_score} ({percentage:.1f}%) ===")