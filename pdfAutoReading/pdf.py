import tabula


# PDFファイルのパス
pdf_file = ".pdf" 

# テキストテーブル取得
df = tabula.read_pdf(pdf_file,       # PDFファイル
                     pages='9',    # 抽出ページ
                     guess=True,     # 分析部分の変更有無
                     area="entire",  # ページの部分指定
                     lattice=False,  # 格子区切りがPDF内にある場合の対応
                     stream=False,   # ストリームモード
                     password=None,  # パスワード
                    )

print(df)