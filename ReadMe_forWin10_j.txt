------------------------------------------------
 TOF-Sensor 結果取得サンプルコード （Python版）
------------------------------------------------

（1）内容
  このコードは、B5L(3D TOFセンサモジュール)のPythonによる結果取得サンプルコードを提供します。
  このサンプルコードでは、「測距開始」、「測距停止」、「結果取得」を実行できます。

（2）ファイルの説明
  TOFSensorSampleGetResult /フォルダーには、次のファイルが存在します。

    TOFSensorSampleGetResult.py         サンプルコードメイン
    tof_serial.py                       シリアルポートの送信/受信クラス
    connect_usb0.sh                     /dev/ttyUSB0と接続するためのshellスクリプト(Ubuntu18専用)

（3）サンプルコードの動作環境
    サンプルコードは、Windows10およびUbuntu18上のPython2.7で動作するように
    コーディングされています。またこのサンプルコードを実行するためには
    モジュール pyserial が必要です。

（4）サンプルコードの実行
     コマンドプロンプトやPowerShellウィンドウにて、
　　 TOFSensorSampleGetResult /フォルダー に移動し、下記のコマンドを実行します。

     python TOFSensorSampleGetResult.py[Enter]
　　 実行画面の詳細については、「ExecutableFileDescription_j.txt」をご参照ください。

【使用上の注意】
* 本サンプルコードおよびドキュメントの著作権はオムロンに帰属します。
* 本サンプルコードは動作を保証するものではありません。
* 本サンプルコードは、Apache License 2.0にて提供しています。

----
オムロン株式会社
Copyright 2020 OMRON Corporation、All Rights Reserved.
