# validation_app

Validation_app is the application based on python programming with PyQt v5 GUI. This application functions to determine whether or not a UAV is precise in carrying out the dot spraying mission. To run this application, UAV (Unmanned Aerial Vehicle) log data and target tree point vectors are needed.

Following are the steps for using the application:

1. The user selects the directory containing the UAV log data via the "Pilih .log" button.
2. Users select the directory containing oil palm plant data in shapefile format via the "Pilih .shp" button.
3. The user selects the directory to save the validation results via the "Pilih hasil" button.
4. The user selects the UTM zone that corresponds to the data collection location.
5. Users select the level of accuracy required for data validation.
6. After selecting all directories and UTM zones, users can press the "Process" button to start the validation process.

Later the results of the process will be grouped into 3 folders, the "merge_drone" folder which contains the UAV flight path per flight, the "merge_tree" folder which contains a collection of target tree points and the "last_result" folder which contains the CSV file of the measurement results.

By using this application, users can easily validate point spraying on oil palm plants by integrating data from UAVs and geospatial data. This can help farmers or plantation managers increase efficiency and accuracy in spraying pesticides or nutrients on oil palm plants.
