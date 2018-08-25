import random

#word:プレーヤーに当ててほしい単語
def hangman(word):
    wrong = 0       #プレーヤーが何回間違えたか
    stages = ["",
              "_______      ",
              "             ",
              "       |     ",
              "       o     ",
              "      /|\    ",
              "      / \    ",
              ]
    rletters = list(word)       #答えの残り文字
    board = ["_"] * len(word)   #ヒント。隠すための_
    win = False                 #True:勝ち, False：負け
    print("ハングマンへようこそ！")

    #勝敗が決まるまでループ。stagesの要素の絵が完成してしまったら負け
    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してちょ:"
        c = input(msg)       #回答
        if c in rletters:
            idx = rletters.index(c)
            board[idx] = c
            rletters[idx] = '$'     #正解文字を＄に置き換え
        else:
            wrong += 1              #不正解回数インクリメント

        #スコアボードを表示
        print(" ".join(board))

        #ハングマンを表示(１行目から間違った回数の行まで)
        e = wrong + 1
        print("\n".join(stages[0:e]))

        #スコアボードに_がなくなったら勝ち
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    #負けたらこっち
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}".format(word))

#３つからランダム
wordlist = ["cat", "dog", "tanuki"]
i = random.randint(0,2)

hangman(wordlist[i])       
