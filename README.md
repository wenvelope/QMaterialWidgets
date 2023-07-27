<p align="center">
  <img width="18%" align="center" src="https://raw.githubusercontent.com/zhiyiYo/QMaterialWidgets/master/docs/source/_static/logo.png" alt="logo">
</p>
  <h1 align="center">
  PySide6-Material-Widgets
</h1>
<p align="center">
  A material design widgets library based on PySide6
</p>

<p align="center">
  <a href="https://pypi.org/project/PySide6-Material-Widgets" target="_blank">
    <img src="https://img.shields.io/pypi/v/pyside6-material-widgets?color=%2334D058&label=Version" alt="Version">
  </a>

  <a style="text-decoration:none">
    <img src="https://static.pepy.tech/personalized-badge/pyside6-material-widgets?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Download"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/License-GPLv3-blue?color=#4ec820" alt="GPLv3"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Win32%20|%20Linux%20|%20macOS-blue?color=#4ec820" alt="Platform Win32 | Linux | macOS"/>
  </a>
</p>

<p align="center">
English | <a href="./docs/README_zh.md">简体中文</a>
</p>

![Interface](https://raw.githubusercontent.com/zhiyiYo/QMaterialWidgets/master/docs/source/_static/Interface.jpg)

## Install
To install Community version:
```shell
pip install PySide6-Material-Widgets -i https://pypi.org/simple/
```

The Community version only provides basic components, while the more advanced ones are available in the [Premium version](https://afdian.net/a/zhiyiYo?tab=shop).

> **Warning**
> Don't install PySide6-Material-Widgets and PySide2-Material-Widgets at the same time, because their package names are all `qmaterialwidgets`.


## Run Example
You can download the executable demo from the [release page](https://github.com/zhiyiYo/QMaterialWidgets/releases).

After installing PySide6-Material-Widgets package using pip, you can run the demo in examples directory, for example:
```python
cd examples/button
python demo.py
```

If you encounter `ImportError: cannot import name 'XXX' from 'qmaterialwidgets'`, it indicates that the imported components are only available in the Premium version.

## Documentation
Want to know more about PySide6-Material-Widgets? Please read the [help document](https://qmaterialwidgets.readthedocs.io/) 👈

## Video Demonstration
Check out this [▶ example video](https://www.bilibili.com/video/BV1k14y1z74o) that shows off what PySide6-Material-Widgets are capable of 🎉

## Work with QtDesigner
You can use PySide6-Material-Widgets in QtDesigner directly by running `python ./tools/designer.py`. If the operation is successful, you should be able to see the PySide6-Material-Widgets in the sidebar of QtDesigner.


## Support
If this project helps you a lot and you want to support the development and maintenance of this project, feel free to sponsor me via [爱发电](https://afdian.net/a/zhiyiYo) or [ko-fi](https://ko-fi.com/zhiyiYo). Your support is highly appreciated 🥰

## Reference
* [**Figma/Material 3 Design Kit**: Provides an introduction to the material design system](https://www.figma.com/community/file/1035203688168086460/Material-3-Design-Kit)
* [**Google/Material Design**: A website demonstrates the controls available in Material Design 3 System](https://m3.material.io/get-started)


## License
PySide6-Material-Widgets adopts dual licenses. Non-commercial usage is licensed under [GPLv3](./LICENSE). For commercial purposes, please purchase on [爱发电](https://afdian.net/a/zhiyiYo?tab=shop) to support the development of this project.

Copyright © 2021 by zhiyiYo.
