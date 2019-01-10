from __future__ import absolute_import, division, print_function, unicode_literals

from madminer.ml import MLForge
import logging
import argparse

logging.basicConfig(
    format='%(asctime)-5.5s %(name)-20.20s %(levelname)-7.7s %(message)s',
    datefmt='%H:%M',
    level=logging.INFO
)
for key in logging.Logger.manager.loggerDict:
    if "madminer" not in key:
        logging.getLogger(key).setLevel(logging.WARNING)


def train(
        filename,
        method='alices',
        tight_cuts=True,
        i=0,
        observables=None,
        n_samples=None,
        n_mades=3,
        n_layers=3,
        alpha=0.001,
        grad_x_regularization=None,
        base_dir='/scratch/jb6504/diboson_mining/',
):
    sample_dir = base_dir + 'data/samples/wgamma_sys/'
    model_dir = base_dir + 'data/models/wgamma_sys/'

    # Labels
    cut_label = '_tight' if tight_cuts else ''
    if method in ["carl", "rolr", "alice", "rascal", "alices"]:
        sample_type = 'ratio'
    elif method in ["nde", "scandal"]:
        sample_type = 'scandal'
    elif method in ["sally", "sallino"]:
        sample_type = 'local'
    else:
        raise ValueError('Unknown method {}'.format(method))

    # Input data
    x_filename = sample_dir + 'train_{}{}/x_train_{}.npy'.format(sample_type, cut_label, i)
    if method in ["nde", "scandal", "sally", "sallino"]:
        theta0_filename = sample_dir + 'train_{}{}/theta0_train_{}.npy'.format(sample_type, cut_label, i)
        y_filename = None
    else:
        theta0_filename = sample_dir + 'train_{}{}/theta_train_{}.npy'.format(sample_type, cut_label, i)
        y_filename = sample_dir + 'train_{}{}/y_train_{}.npy'.format(sample_type, cut_label, i)
    if method in ["rascal", "alices", "sally", "sallino", "scandal"]:
        t_xz0_filename = sample_dir + 'train_{}{}/t_xz_train_{}.npy'.format(sample_type, cut_label, i)
    else:
        t_xz0_filename = None
    if method in ["rolr", "rascal", "alice", "alices"]:
        r_xz_filename = sample_dir + 'train_{}{}/r_xz_train_{}.npy'.format(sample_type, cut_label, i)
    else:
        r_xz_filename = None

    # Network architecture
    n_hidden = tuple([100 for _ in range(n_layers)])

    # Train model
    ml = MLForge()

    ml.train(
        method=method,
        x_filename=x_filename,
        theta0_filename=theta0_filename,
        t_xz0_filename=t_xz0_filename,
        r_xz_filename=r_xz_filename,
        y_filename=y_filename,
        features=observables,
        nde_type='mafmog',
        maf_mog_n_components=10,
        maf_n_mades=n_mades,
        n_hidden=n_hidden,
        activation="tanh",
        alpha=alpha,
        trainer="amsgrad",
        n_epochs=50,
        batch_size=256,
        initial_lr=0.001,
        final_lr=0.0001,
        validation_split=0.5,
        grad_x_regularization=grad_x_regularization,
        limit_samplesize=n_samples,
    )

    ml.save(model_dir + '{}_{}_{}'.format(method, filename, i), True)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Likelihood-free inference experiments with gold from the simulator')

    parser.add_argument('filename', type=str)
    parser.add_argument('method', type=str)
    parser.add_argument('run', type=int)
    parser.add_argument('--loose', action='store_true')
    parser.add_argument('--observables', type=int, nargs='+', default=None)
    parser.add_argument('--samples', type=int, default=None)
    parser.add_argument('--mades', type=int, default=3)
    parser.add_argument('--layers', type=int, default=3)
    parser.add_argument('--alpha', type=float, default=0.001)
    parser.add_argument('--gradx', type=float, default=None)

    args = parser.parse_args()

    # Start simulation
    train(
        filename=args.filename,
        method=args.method,
        tight_cuts=not args.loose,
        i=args.run,
        observables=args.observables,
        n_samples=args.samples,
        n_layers=args.layers,
        alpha=args.alpha,
        grad_x_regularization=args.gradx,
    )
