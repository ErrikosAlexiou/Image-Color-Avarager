def ScreenSize(screenWidth, screenHeight):
    appSizeW = screenWidth / 2
    appSizeH = screenHeight / 2

    appWpos = screenWidth / 4
    appHpos = screenHeight / 4

    appGeometry = (
        int(appSizeW),
        "x",
        int(appSizeH),
        "+",
        int(appWpos),
        "+",
        int(appHpos),
    )

    appGeometry = str(appGeometry).replace(" ", "")
    appGeometry = str(appGeometry).replace("'", "")
    appGeometry = str(appGeometry).replace(",", "")
    appGeometry = str(appGeometry).replace("(", "")
    appGeometry = str(appGeometry).replace(")", "")

    return appGeometry
