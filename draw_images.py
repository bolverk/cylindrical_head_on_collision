def main():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import glob
    import h5py
    import numpy

    fname_list = glob.glob('output/snapshot_*.h5')
    for fname in fname_list:
        print(fname)
        with h5py.File(fname,'r') as f:
            x_list = numpy.array(f['geometry']['x_coordinate'])
            y_list = numpy.array(f['geometry']['y_coordinate'])
            d_list = numpy.array(f['hydrodynamic']['density'])
            time = numpy.array(f['time'])[0]
        z_list = numpy.log10(d_list)
        fig, ax = plt.subplots()
        fig.suptitle('Density @ t = %2.2f' % time)
        con = ax.tricontourf(x_list, y_list, z_list, 50)
        ax.autoscale_view()
        ax.set_aspect('equal')
        fig.colorbar(con)
        fig.savefig(fname.replace('snapshot','density').replace('h5','png'))
        plt.close(fig)

if __name__ == '__main__':

    main()
