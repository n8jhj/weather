import os
import shutil

from weather import weather

def test_library_creation(tmpdir):
    lib_name = 'library'
    # Move important data to temporary directory.
    os.rename(lib_name, tmpdir.join(lib_name))
    # Initialize.
    app = weather.WeatherApp()
    temp_data = app.get_data()
    # Library should not exist initially.
    assert not os.path.isdir(lib_name)
    app.save(temp_data)
    # Library should exist after save.
    assert os.path.isdir(lib_name)
    assert os.path.isfile(os.path.join(lib_name, 'data.json'))
    # Restore important data.
    shutil.rmtree(lib_name)
    tmpdir.join(lib_name).rename(lib_name)
    # Delete temporary directory.
    tmpdir.join('..').remove()
