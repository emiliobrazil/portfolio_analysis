import matplotlib.pyplot as plt


class PortfolioFig:
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.title = None
        self.Y_title = None
        self.X_title = None
        self.labels = None
        self.grid_check = False
        self.bgcollor = None


    def set_axletitle(self, axle, title):
        if axle in ["y", "Y", "V", "v", "vertical"]:
            self.Y_title = title
        if axle in ["x", "X", "H", "H", "horizontal"]:
            self.X_title = title

    def set_labels(self, labels):
        self.labels = labels

    def set_title(self, title):
        self.title = title

    def set_grid(self, want_grid):
        self.grid_check = want_grid

    def set_bgcollor(self, collor):
        self.bgcollor = collor

    def fig_cache(self, cache_path, lblshow=False):
        # Itera sobre as listas de dados e plota cada linha
        plt.rc('font', size=42)
        if lblshow:

            plt.plot(self.x_axis, self.y_axis, label=self.labels[i - 1])
            plt.legend()
        else:

            plt.plot(self.x_axis, self.y_axis)

        # Adiciona legendas e rótulos

        plt.xlabel(self.X_title)
        plt.ylabel(self.Y_title)
        if self.bgcollor is not None:
            plt.gca().set_facecolor(self.bgcollor)
        if self.grid_check:
            plt.grid(True)
        if self.title is not None:
            plt.title(self.title)
        fig = plt.gcf()

        fig.set_size_inches(1920 / 100, 1080/ 100)  # Convertendo de pixels para polegadas
        plt.xticks([self.x_axis[0],self.x_axis[-1]])
        # Salvar a figura em um arquivo PNG com DPI personalizado
        plt.savefig('exemplo.png', dpi=500)
        plt.savefig(cache_path)


if __name__ == "__main__":
    print("teste fora")
    ax = [1, 2, 3, 4]
    y1 = [1, 2, 4, 8]
    y2 = [1, 2, 3, 4]
    y3 = [0, 0, 5, 20]

    figura = PortfolioFig(ax, [y1, y2, y3])
    figura.set_title("TTITULO")
    figura.set_axletitle("x","eixo x")
    figura.set_axletitle("y", "eixo y")
    figura.set_bgcollor("lightblue")
    figura.fig_cache("")
