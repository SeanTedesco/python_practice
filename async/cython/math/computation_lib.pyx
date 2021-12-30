from libc.math cimport sqrt
import cython

def do_math(start: cython.int = 0, num: cython.int = 10):
    pos: cython.int = start
    k_sq: cython.int = 1000 * 1000
    dist: cython.int = 0
    with nogil:
        while pos < num:
            pos += 1
            dist = sqrt((pos - k_sq)*(pos - k_sq))