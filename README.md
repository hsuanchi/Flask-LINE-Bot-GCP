# Flask-LINE-Bot-GCP

### 一. 建立 LINE-Bot 機器人

#### 1.事前準備

首先建立 LINE develops 帳戶，請參考這篇 [Flask – LINE Bot 教學 事前準備篇 (一)](https://www.maxlist.xyz/2020/11/16/flask-line-bot-pre-set/)
* 確認取得 Channel secret
* 確認取得 Channel access token

#### 2. 建立 Project
這次的範例 Code，都存放在這邊 [Flask-LINE-Bot-GCP](https://github.com/hsuanchi/Flask-LINE-Bot-GCP)，歡迎給星和 Fork 使用

2.1 先移動到資料夾 flask 的位置
```
$ cd /Flask-LINE-Bot-GCP/flask/
```

接下來我們會在資料夾中建立 `.flaskenv` 並將 token 環境變數放進去：
```
$ vim .flaskenv
```

```
export CHANNEL_ACCESS_TOKEN="/pg7A9LjzlJ0Bxxxx...省略...cDnyilFU="
export CHANNEL_SECRET='9c5d20481...省略...f81f'
```


2.2 再來需要建立 SSL Certificates，因為 LINE 只接收 Https 的協議，
建議可以使用 https://www.sslforfree.com/ 提供的 SSL Certificates

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-GCP/blob/main/img/sslforfree.png" width="800px" height="auto">
將拿到的 ssl.csr 和 ssl.key 放在 `nginx` 資料夾中就完成，最後就只剩下部署到 GCP 上囉！

### 二. 建立 GCP 虛擬主機

在 [Google Cloud Platform](https://cloud.google.com/gcp/?hl=zh-tw) > 選 Compute Engine > 選建立 VM 執行個體，接下來會進入如下附圖畫面：
<img src="https://github.com/hsuanchi/Flask-LINE-Bot-GCP/blob/main/img/step1%20create%20gcp%20server.png" width="800px" height="auto">


1. 選擇想要的地區
2. 選擇想要的機器類型
3. 下方防火牆部分，要把允許 HTTP & HTTPS 流量打勾

筆者推薦主機部分可以選擇以下三個美國地區，和主機類型選 f1-micro VM 主機 (1 vCPU，0.6 GB 記憶體)，因為會適用於 GCP 免費方案 (過試用期後，不會收費)，可以參考 [Google 官方文件](https://cloud.google.com/free/docs/gcp-free-tier?hl=zh-TW#always-free) 說明：

* 奧勒岡州：us-west1
* 愛荷華州：us-central1
* 南卡羅來納州：us-east1

### 三. 開始部署 LINE-Bot 於 GCP 上

建置好主機後，點擊下圖紅框框內 SSH 進入連線

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-GCP/blob/main/img/step2%20gcp%20ssh%20%E9%80%A3%E7%B7%9A.png" width="800px" height="auto">



首先先將權限切換到 root，待會安裝比較方便：
```
$ sudo su
```

接下來我們會需要安裝 git & docker & docker-compose
1.安裝 Git
```
$ sudo apt-get install git
```
2.安裝 curl & Docker
```
$ sudo apt-get install -y curl
$ curl -s https://get.docker.com | sudo sh
```
3.安裝 [docker-compose](https://docs.docker.com/compose/install/)

```
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

$ sudo chmod +x /usr/local/bin/docker-compose
```
4.將剛剛建立好的專案 git clone 到虛擬主機中
```
$ git clone https://github.com/hsuanchi/Flask-LINE-Bot-GCP.git
```

5.移動到資料節內，並使用 docker-compose 啟動
```
$ cd Flask-LINE-Bot-GCP
$ docker-compose up --build
```


最後只需要將 ip 位置放在 LINE 的 webhook url 上完成啦！

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-GCP/blob/main/img/line-bot%20webhook-url.png" width="800px" height="auto">


本篇文章同步刊登於 [ [Flask 教學] LINE-Bot GCP 部署(Docker+Flask+Nginx)](https://www.maxlist.xyz/2020/12/01/flask-line-bot-docker-flask-nginx-gcp/)，如果有遇到任何問題，歡迎私訊或留言，我會盡快回覆您
