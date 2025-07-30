from era2grads import PressureLevelDownloader, SingleLevelDownloader
from era2grads import NCDFormatter
import os



surface_downloader = SingleLevelDownloader()
surface_downloader.download(
    variables=['10m_u_component_of_wind', '2m_temperature', '10m_v_component_of_wind'],
    year=2024,
    month=2,
    days=[14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    area=[-15, -60, -45, -33],
    time=['00:00'],
    output_file="datos/u10_v10_t2m.nc"
)

surface_downloader.download(
    variables=['Total precipitation', 'Convective precipitation'],
    year=2024,
    month=2,
    days=[14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    area=[-15, -60, -45, -33],
    time=['00:00'],
    output_file="datos/precip.nc"
)

surface_downloader.download(
    variables=['Mean sea level pressure'],
    year=2024,
    month=2,
    days=[14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    area=[-15, -60, -45, -33],
    time=['00:00'],
    output_file="datos/mslp.nc"
)




