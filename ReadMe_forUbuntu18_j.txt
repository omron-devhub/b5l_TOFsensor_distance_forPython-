------------------------------------------------
 TOF-Sensor 結果取得サンプルコード （Python版）
------------------------------------------------

（1）内容
  このコードは、TOFセンサーのPython版結果取得サンプルコードを提供します。
  このサンプルコードでは、「測距開始」、「測距停止」、「結果取得」を実行できます。

  注)本サンプルコードは、お客様でコーディングされる際の参考用としてご利用ください。
     結果取得したデータをファイル出力することはできません。
     以下のようにTOFSensorSampleGetResult.py内のser.log_shapeの引数をTrueに変更することで、
     結果取得したデータを画面出力することはできますが、出力完了するまでに非常に時間がかかります。
           Line 97 : data = ser.log_shape(False)　⇒　data = ser.log_shape(True)
           Line 120 :  ser.log_shape(False)　⇒　data = ser.log_shape(True)

     性能評価をされる場合は、下記のURLより評価用ソフトウェアをダウンロードしてご利用ください。
     https://www.omron.co.jp/ecb/sensors/displacement-sensors_ranging-sensors/3D-TOF-sensor-module/B5L_licence

（2）ファイルの説明
  TOFSensorSampleGetResult /フォルダーには、次のファイルが存在します。

    TOFSensorSampleGetResult.py         サンプルコードメイン
    tof_serial.py                       シリアルポートの送信/受信クラス
    connect_usb0.sh                     /dev/ttyUSB0と接続するためのshellスクリプト(Ubuntu18専用)

（3）サンプルコードの動作環境
    サンプルコードは、Windows10およびUbuntu18上のPython2.7で動作するように
    コーディングされています。またこのサンプルコードを実行するためには
    モジュール pyserial が必要です。

（4）実行前の準備
    [/dev/ttyUSB0の設定]

    shellにて以下のように入力してください

    sudo modprobe usbserial vendor=0x0590 product=0x00ca[Enter]
    sudo chmod o+wr /dev/ttyUSB0[Enter]

    または以下のファイルに実行権限を与えて実行してください

    connect_usb0.sh

（5）サンプルコードの実行
    shellにてTOFSensorSampleGetResult /フォルダーに移動し、下記のコマンドを実行します。

    python TOFSensorSampleGetResult.py[Enter]
    実行画面の詳細については、「ExecutableFileDescription_j.txt」をご参照ください。


【使用上の注意】
* 本サンプルコードおよびドキュメントの著作権はオムロンに帰属します。
* 本サンプルコードは動作を保証するものではありません。
* 本サンプルコードは、Apache License 2.0にて提供しています。

----
オムロン株式会社
Copyright 2020-2021 OMRON Corporation、All Rights Reserved.