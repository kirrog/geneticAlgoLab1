from matplotlib import pyplot as plt

if __name__ == "__main__":
    with open("results.tsv", "r") as f:
        data = [x.split("\t") for x in f.read().split("\n")][1:-1]

        # Time heatmap
        heatmap_time = [[0.0] * 10 for x in range(10)]
        maximum_time = max(max([float(x[2]) for x in data]), max([float(x[3]) for x in data]))
        minimum_time = min(min([float(x[2]) for x in data]), min([float(x[3]) for x in data]))
        time_range = maximum_time - minimum_time
        for up_level_iter, count_iter, default_time_accum, optimised_time_accum, default_mem_accum, optimised_mem_accum in data:
            up_i = int(int(up_level_iter) / 1000) - 1
            count_i = int(int(count_iter) / 1000) - 1
            heatmap_time[up_i][count_i] = (float(default_time_accum) - float(optimised_time_accum)) / time_range
        plt.imshow(heatmap_time)
        plt.colorbar()
        plt.title("Heatmap of time difference")
        plt.savefig("Heatmap of time difference")
        # plt.show()
        plt.close()

        # Memory heatmap
        heatmap_mem = [[0.0] * 10 for x in range(10)]
        maximum_mem = max(max([float(x[4]) for x in data]), max([float(x[5]) for x in data]))
        minimum_mem = min(min([float(x[4]) for x in data]), min([float(x[5]) for x in data]))
        time_range = maximum_mem - minimum_mem
        for up_level_iter, count_iter, default_time_accum, optimised_time_accum, default_mem_accum, optimised_mem_accum in data:
            up_i = int(int(up_level_iter) / 1000) - 1
            count_i = int(int(count_iter) / 1000) - 1
            heatmap_mem[up_i][count_i] = (float(default_mem_accum) - float(optimised_mem_accum)) / time_range
        plt.imshow(heatmap_mem)
        plt.colorbar()
        plt.title("Heatmap of memory difference")
        plt.savefig("Heatmap of memory difference")
        # plt.show()
        plt.close()

        # Plot of times
        for up_ in ["01000", "10000"]:
            x = [x[1] for x in data if x[0] == up_]
            y_d = [float(x[2]) for x in data if x[0] == up_]
            y_o = [float(x[3]) for x in data if x[0] == up_]
            plt.plot(x, y_d, 'g', label="default")
            plt.plot(x, y_o, 'b', label="optimised")
            plt.xlabel("n")
            plt.ylabel("Average time")
            plt.legend()
            plt.title(f"Plot time up lvl {up_}")
            plt.savefig(f"Plot time up lvl {up_}")
            # plt.show()
            plt.close()
        for count_ in ["01000", "10000"]:
            x = [x[0] for x in data if x[1] == count_]
            y_d = [float(x[2]) for x in data if x[1] == count_]
            y_o = [float(x[3]) for x in data if x[1] == count_]
            plt.plot(x, y_d, 'g', label="default")
            plt.plot(x, y_o, 'b', label="optimised")
            plt.xlabel("k")
            plt.ylabel("Average time")
            plt.legend()
            plt.title(f"Plot time count {count_}")
            plt.savefig(f"Plot time count {count_}")
            # plt.show()
            plt.close()

        # plot of memory
        for up_ in ["01000", "10000"]:
            x = [x[1] for x in data if x[0] == up_]
            y_d = [float(x[4]) for x in data if x[0] == up_]
            y_o = [float(x[5]) for x in data if x[0] == up_]
            plt.plot(x, y_d, 'g', label="default")
            plt.plot(x, y_o, 'b', label="optimised")
            plt.xlabel("n")
            plt.ylabel("Average time")
            plt.legend()
            plt.title(f"Plot mem up lvl {up_}")
            plt.savefig(f"Plot mem up lvl {up_}")
            # plt.show()
            plt.close()
        for count_ in ["01000", "10000"]:
            x = [x[0] for x in data if x[1] == count_]
            y_d = [float(x[4]) for x in data if x[1] == count_]
            y_o = [float(x[5]) for x in data if x[1] == count_]
            plt.plot(x, y_d, 'g', label="default")
            plt.plot(x, y_o, 'b', label="optimised")
            plt.xlabel("k")
            plt.ylabel("Average time")
            plt.legend()
            plt.title(f"Plot mem count {count_}")
            plt.savefig(f"Plot mem count {count_}")
            # plt.show()
            plt.close()
