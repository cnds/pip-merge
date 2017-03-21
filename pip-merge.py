import os
from docopt import docopt
from pip.req import parse_requirements
from pip.index import PackageFinder
from pip._vendor.requests import session

requests = session()


class Requirements(object):
    def __init__(self, reqfile=None):
        super(Requirements, self).__init__()
        self.path = reqfile
        self.requirements = list()

        if reqfile:
            self.laod(reqfile)

    def __repr__(self):
        return "<Requirements {} >".format(self.path)

    def load(self, reqfile):
        if not os.path.exists(reqfile):
            raise ValueError('The given requirements file does not exist.')

        finder = PackageFinder([], [], session=requests)
        for requirement in parse_requirements(reqfile, finder=finder, session=requests):
            if requirement.req:
                if not getattr(requirement.req, 'name', None):
                    requirement.req.name = requirement.req.project_name
                self.requirements.append(requirement.req)

    def merge(self, requirements, ignore_versions=False):
        r1 = self
        r2 = requirements
        results = {'new': [], 'old': []}

        if ignore_versions:
            for r in r1.requirements:
                results['new'].append(r.name)
            for req in r2.requirements:
                r = req.name
                if r not in results['new']:
                    results['new'].append(r)


def merge(r1, r2, ignore_versions=False, include_new=False, include_old=False):
    try:
        r1 = Requirements(r1)
        r2 = Requirements(r2)
    except ValueError:
        print 'loading requirements files error'
        exit(os.EX_NOINPUT)

    results = r1.merge(r2, ignore_versions=True)
    if include_new:
        for line in results['new']:
            print line


def main():
    args = docopt(__doc__, version='pip-merge')

    kwargs = {
        'r1': args['<reqfile1>'],
        'r2': args['<reqfile2>'],
        'include_new': args['--new'],
        'include_old': args['--old']
    }

    merge(**kwargs)


if __name__ == '__main__':
    main()
