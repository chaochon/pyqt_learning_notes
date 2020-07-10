# 1.qss的概念

风格样式表，用于自定义控件外观的机制

# 2.语法

基本语法由两个部分组成：选择器和声明。选择器用于指定某个或某类控件，声明由一些属性值对
组成，由;分割，用于说明控件外观样式。

```
QPushButton {color:red}
QPushButton,QLineEdit,QComboBox {color: red}  // 指定多个选择器
```

## 选择器类型

1. 通配选择器：*
2. 类型选择器：QPushButton 指定QPushButton控件及其子控件
3. 属性选择器：QPushButton[name=myname] 指定QPushButton控件中name属性为myname的部件
4. 类选择器：  .QPushButton 指定QPushButton控件，但不指定其子类
5. id选择器：  #myButton 指定ObjectName=myButton的部件
6. 后代选择器： QDialog QPushButton 指定容器中的部件
7. 子选择器：   QDialog>QPushButton 指定容器中的部件，此外要求部件中的

## 伪状态

伪状态是一个部件或者复合部件的部分部件处于某种状态时，触发QSS规则。
用法：
```
QComboBox:hover{background-color:white}  //在选择器后面接: 指定状态条件
``` 

## 设置背景图片

```buildoutcfg
#MainWindow{border-image:url(image/python.jpg);background-color:white}
```

## 设置窗体透明度

```buildoutcfg
self.setWindowOpacity(0.5)   # 设置透明度
```


