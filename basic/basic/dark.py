class MyMat:

    def __init__(self):
        pass

    def cli(x, y, z):
        import matplotlib.pyplot as plt
        # x = [1, 2, 3, 4]
        # y = [5, 4, 3, 2]
        plt.figure()
        # plt.figure(figsize=(30,20))
        plt.subplot(231)
        plt.plot(x, y)
        plt.subplot(232)
        plt.bar(x, y)
        plt.subplot(233)
        plt.barh(x, y)
        plt.subplot(234)
        plt.bar(x, y)
        plt.bar(x, z, bottom=y, color='r')
        plt.subplot(235)
        plt.boxplot(x)
        # 绘制盒图
        plt.subplot(236)
        plt.scatter(x, y)
        plt.gcf().set_size_inches(18.5, 10.5)
        plt.gcf().savefig('test2.png', dpi=100)
        plt.show()

if __name__ == "__main__":
    newMyMat = MyMat
    newMyMat.cli([111, 22, 33, 11], [22, 22, 33, 11], [7, 8, 5, 3])
