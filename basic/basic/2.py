class MyMat:

    def __init__(self):
        pass

    def cli(x, y):
        import matplotlib.pyplot as plt
        # x = [1, 2, 3, 4]
        # y = [5, 4, 3, 2]
        plt.figure()
        plt.subplot(231)
        plt.plot(x, y)
        plt.subplot(232)
        plt.bar(x, y)
        plt.subplot(233)
        plt.barh(x, y)
        plt.subplot(234)
        plt.bar(x, y)
        y1 = [7, 8, 5, 3]
        plt.bar(x, y1, bottom=y, color='r')
        plt.subplot(235)
        plt.boxplot(x)
        # 绘制盒图
        plt.subplot(236)
        plt.scatter(x, y)
        plt.show()


if __name__ == "__main__":
    newMyMat = MyMat()
    MyMat.cli([11, 22, 33, 44], [22, 33, 11, 11])
