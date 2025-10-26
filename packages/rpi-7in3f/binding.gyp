{
    "targets": [
        {
            "target_name": "waveshare7in3f",
            "cflags!": [
                "-fno-exceptions",
                "-Wextra"
            ],
            "cflags_cc!": [ "-fno-exceptions" ],
            "sources": [ 
                "./src/c/EPD_7in3f_node.cc",
                "./src/c/EPD_7in3f.c",
                "./src/c/DEV_Config.c"
            ],
            "defines": [
                "RPI",
                "USE_LGPIO_LIB"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "libraries": [
                "-lm",
                "-llgpio"
            ]
        }
    ]
}
