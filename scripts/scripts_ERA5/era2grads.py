from era2grads import NCDFormatter

formatter = NCDFormatter()
formatter.grads_optimize(
    input_file="datos/output.nc",
    output_file="datos_grads/output_grads.nc",
    rename_dict={'latitude': 'lat', 'longitude': 'lon'},
    cdo_compression="-f nc4c -z zip_4"
)


