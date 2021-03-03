# README

本项目为 **湖南大学打卡系统每日自动打卡**

在 **0点，3点，7点的20分及50分** 各尝试打卡

每次尝试登陆和打卡次数通过`main.py`的参数控制，默认各 **5** 次，如有需求可以自行更改，包括打卡时间，及是否在家选项，**详见步骤4**

如果这几次都失败了，说明湖大服务器又gg了，第二天会有电话提醒还有各种@，这里就不做额外提醒了:)

欢迎Star~

## 项目结构

```shell
HNUClockIn
│  hnu_clockin.py
│  main.py
│  README.md
│  read_inform.py
│  vcode_img.py
│  vocr.py
│
└─config
  config.py
  inform.json
  clockin.yml
```

## 操作指南

> 如果身体出现疑似症状或者途径风险地区等时
>
> 请手动上报，勿使用自动自动打卡
>
> 防疫人人有责

### 0. 注册Github账号并下载配置Github

本项目基于Github Actions，因此一个Github账号是必要的

[下载Github](https://gitforwindows.org/)

### 0.1. 配置Github

1. 安装完Github后，在桌面右键选择`Git Gui Here`

2. 进去之后，选择左上角的`help`选项，会出现一个`Show SSH Key`，然后点击`Generate Key`得到秘钥。将其复制到剪切板

3. 打开`GitHub`网页，登陆后，点击右上角头像，打开`Settings`设置界面，在`SSH and GPG Keys`栏中点击`Add SSH key`按钮，然后粘贴上面生成的秘钥，点击`add key`

4. 此时便可以开始使用Git功能了，右键桌面，选择`Git Bash Here`，进去后便可进入Git控制台，进行用户账户信息的配置：

   `git config --global user.name "你的Github用户名"`

   `git config --global user.email "你的Github邮箱地址"`

### 1. Clone本仓库到本地

1. 在你打算存放本项目的地方，右键选择`Git Bash Here`

2. 输入`git clone https://github.com/Brokenice0415/HNUClockIn`

### 2. 注册百度智能账号，获取api

[进入百度智能OCR](https://console.bce.baidu.com/ai/#/ai/ocr/overview/index)

1. 注册后在个人主页控制台点击 **创建应用** 

2. 随便写个应用名称，接口选择 **文字识别**

3. 然后就可以看到所给的`APP ID`，`API Key`，`Secret Key`

### 3. 修改inform.json

使用**记事本**等软件打开本项目中的`config/inform.json`

在引号中填入自己的相关信息

- `hnu_account`: 湖南大学个人门户的账号密码

- `baidu_ai_account`: 填入刚才所注册的百度智能账号的`APP ID`，`API Key`，`Secret Key`
- `clockin_inform`: 在家打卡时所要填写的信息，包括省，市，县和在家及在校的详细地址

### 4. 修改clockin.yml

使用**记事本**等软件打开本项目中的`config/clockin.yml`

1. 修改打卡时间

   在第8行`- cron: '20,50 16,19,23 * * *'`

   其中`20,50`表示第20和50分钟

   `16,19,23`表示UTC时区的第16，19，23小时，也就是北京时间0点，3点和7点

   由于是每天打卡，后面的三个`*`不需要更改

   > 比如需要修改为每天北京时间1点23分打卡，则修改第8行为
   >
   > ````yaml
   > -cron: '23 17 * * *'
   > ````

2. 修改每次打卡尝试次数

   **每次打卡尝试次数表示每次运行程序所进行的尝试次数，运行次数通过上面的打卡时间设置**

   在第28行`python main.py --at_home 0`

   修改最大登陆尝试次数，在后面添加`--login_max_try 次数`

   修改最大打卡尝试次数，在后面添加`--clockin_max_try 次数`

   > 比如需要修改为最大登陆尝试次数10次，最大打卡尝试次数8次，则修改第28行为
   >
   > ```yaml
   > python main.py --at_home 0 --login_max_try 10 --clockin_max_try 8
   > ```

3. 修改打卡位置选项

   ~~众所周知~~，湖大打卡分在校和在家两种模式

   因此通过at_home参数来控制这两种模式，1即为在家，0即为在校

   > 比如需要修改为在家模式，则修改第28行为
   >
   > ```yaml
   > python main.py --at_home 0 --login_max_try 10 --clockin_max_try 8
   > ```
   >
   > 或者（因为默认at_home为1，不输入参数也可
   >
   > ```yaml
   > python main.py
   > ```

### 5. Publish本地仓库到Github

不熟悉Git指令的可以使用[Git Desktop](https://desktop.github.com/)

打开后点击`File->Add local repository`将刚刚clone的仓库添加到你的仓库

**记得设置仓库私有(private)** ~~(默认私有)~~

然后点击右上角`Publish`，直到显示`Fetch origin`即发布完毕

### 6. 添加Action

1. 在网页上打开Github，在Repository中找到刚刚创建的仓库，进入后点击Actions
2. 然后点击`set up a workflow yourself ->`，会弹出一个在线文本编辑
3. 将刚刚修改过的`config/clockin.yml`的全部拷入覆盖
4. 点击右上角`Commit`
5. 在Actions中出现名`HNUClockIn`的workflow即为配置完毕
