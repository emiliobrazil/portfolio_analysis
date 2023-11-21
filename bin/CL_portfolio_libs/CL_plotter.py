import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from time import time

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
        plt.rc('font', size=20)
        if self.y_axis[0]>self.y_axis[-1]:
            line_color='red'
        else:
            line_color='green'
        if lblshow:

            plt.plot(self.x_axis, self.y_axis, label=self.labels[i - 1])
            plt.legend()
        else:

            plt.plot(self.x_axis, self.y_axis,color=line_color,linewidth=5)


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
        plt.grid(True, color='white')

        fig.set_size_inches(400 / 40, 225/ 40)  # Convertendo de pixels para polegadas
        plt.xticks([self.x_axis[0],self.x_axis[-1]])

        # Salvar a figura em um arquivo PNG com DPI personalizado
        plt.savefig(cache_path, dpi=40)
        plt.close()

class SimulationFig:
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
        plt.rc('font', size=20)

        if lblshow:
            for i in range(len(self.y_axis)-1):

                plt.plot(self.x_axis, self.y_axis[i], label=self.labels[i - 1])
                plt.legend()
        else:
            for i in range(len(self.y_axis)):
                if self.y_axis[i][0] > self.y_axis[i][-1]:
                    line_color = 'red'
                else:
                    line_color = 'green'

                plt.plot(self.x_axis, self.y_axis[i],color=line_color,linewidth=5)


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

        fig.set_size_inches(400 / 50, 225/ 50)  # Convertendo de pixels para polegadas
        plt.xticks([self.x_axis[0],self.x_axis[-1]])

        # Salvar a figura em um arquivo PNG com DPI personalizado
        plt.savefig(cache_path, dpi=50)
        plt.close()

