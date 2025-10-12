from data_generator import generate_synthetic_transit_data

def test_data_generation():
    df = generate_synthetic_transit_data()
    assert len(df) == 500
    assert "Trip_ID" in df.columns
    assert df["Trip_ID"].is_unique