# """Methods for testing the subroutines in the structures module."""
# import unittest as ut

# # def TestMakeEnumIn(ut.TestCase):
# #     """Tests the make_enum_in subroutine."""

# #     def MakeEnumIn1(self):
# #         from phenum.structures import make_enum_in

# class TestDistribute(ut.TestCase):
#     """Tests of the _distribute subroutine."""

#     def testDistribute1(self):
#         from phenum.structures import _distribute
#         out = {(4, (1, 0, 1, 1, 1, 4), (2, 2)): 2, (4, (1, 0, 2, 1, 0, 2), (2, 2)): 3, (2, (1, 0, 1, 0, 1, 2), (0, 2)): 1, (4, (1, 0, 1, 0, 1, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 1, 4), (0, 4)): 1, (3, (1, 0, 1, 0, 0, 3), (1, 2)): 1, (3, (1, 0, 1, 0, 1, 3), (1, 2)): 1, (2, (1, 0, 1, 0, 0, 2), (1, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (4, 0)): 1, (3, (1, 0, 1, 0, 0, 3), (0, 3)): 1, (4, (1, 0, 1, 1, 2, 4), (3, 1)): 1, (4, (1, 0, 2, 1, 0, 2), (0, 4)): 1, (4, (1, 0, 2, 0, 0, 2), (1, 3)): 1, (4, (1, 0, 1, 1, 1, 4), (3, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (0, 4)): 1, (4, (1, 0, 2, 1, 0, 2), (1, 3)): 1, (4, (1, 0, 1, 0, 0, 4), (0, 4)): 1, (4, (1, 0, 1, 0, 0, 4), (1, 3)): 1, (3, (1, 0, 1, 0, 0, 3), (2, 1)): 1, (3, (1, 0, 1, 1, 1, 3), (2, 1)): 1, (4, (1, 0, 1, 0, 0, 4), (2, 2)): 2, (4, (1, 0, 2, 1, 0, 2), (4, 0)): 1, (2, (1, 0, 1, 1, 1, 2), (1, 1)): 1, (3, (1, 0, 1, 1, 1, 3), (1, 2)): 1, (4, (1, 0, 1, 1, 1, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 2, 4), (1, 3)): 1, (3, (1, 0, 1, 0, 0, 3), (3, 0)): 1, (4, (1, 1, 2, 1, 0, 2), (0, 4)): 1, (2, (1, 0, 1, 0, 1, 2), (2, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (2, 2)): 2, (2, (1, 0, 1, 1, 1, 2), (2, 0)): 1, (4, (1, 0, 1, 0, 0, 4), (4, 0)): 1, (4, (1, 0, 1, 0, 1, 4), (2, 2)): 2, (4, (1, 0, 1, 0, 1, 4), (3, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (2, 2)): 1, (4, (1, 0, 1, 0, 2, 4), (3, 1)): 1, (2, (1, 0, 1, 0, 1, 2), (1, 1)): 1, (4, (1, 0, 1, 1, 2, 4), (0, 4)): 1, (3, (1, 0, 1, 0, 1, 3), (2, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (1, 3)): 1, (2, (1, 0, 1, 0, 0, 2), (0, 2)): 1, (4, (1, 0, 1, 2, 2, 4), (2, 2)): 2, (4, (1, 0, 2, 0, 0, 2), (4, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (3, 1)): 1, (3, (1, 0, 1, 0, 1, 3), (0, 3)): 1, (4, (1, 0, 1, 0, 1, 4), (1, 3)): 1, (2, (1, 0, 1, 0, 0, 2), (2, 0)): 1, (4, (1, 1, 2, 1, 0, 2), (4, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (0, 4)): 1, (4, (1, 0, 2, 0, 0, 2), (0, 4)): 1, (3, (1, 0, 1, 1, 1, 3), (3, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (1, 3)): 1, (4, (1, 1, 2, 1, 0, 2), (3, 1)): 1, (2, (1, 0, 1, 1, 1, 2), (0, 2)): 1, (4, (1, 0, 2, 0, 0, 2), (2, 2)): 2, (4, (1, 0, 1, 1, 1, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 1, 4), (0, 4)): 1, (4, (1, 0, 2, 1, 0, 2), (3, 1)): 1, (1, (1, 0, 1, 0, 0, 1), (1, 0)): 1, (3, (1, 0, 1, 1, 1, 3), (0, 3)): 1, (3, (1, 0, 1, 0, 1, 3), (3, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (4, 0)): 1, (1, (1, 0, 1, 0, 0, 1), (0, 1)): 1, (4, (1, 0, 2, 0, 0, 2), (3, 1)): 1, (4, (1, 0, 1, 0, 0, 4), (3, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (2, 2)): 2}
#         self.assertEquals(out,_distribute([1, 2, 3, 4], 'all',dataformat= 'tests/enumeration/sc_1/cells.{}', seed=1010))

#     def testDistribute2(self):
#         from phenum.structures import _distribute
#         out = {(4, (1, 0, 1, 1, 1, 4), (2, 2)): 2, (4, (1, 0, 2, 1, 0, 2), (2, 2)): 3, (2, (1, 0, 1, 0, 1, 2), (0, 2)): 1, (4, (1, 0, 1, 0, 1, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 1, 4), (0, 4)): 1, (3, (1, 0, 1, 0, 0, 3), (1, 2)): 1, (3, (1, 0, 1, 0, 1, 3), (1, 2)): 1, (2, (1, 0, 1, 0, 0, 2), (1, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (4, 0)): 1, (3, (1, 0, 1, 0, 0, 3), (0, 3)): 1, (4, (1, 0, 1, 1, 2, 4), (3, 1)): 1, (4, (1, 0, 2, 1, 0, 2), (0, 4)): 1, (4, (1, 0, 2, 0, 0, 2), (1, 3)): 1, (4, (1, 0, 1, 1, 1, 4), (3, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (0, 4)): 1, (4, (1, 0, 2, 1, 0, 2), (1, 3)): 1, (4, (1, 0, 1, 0, 0, 4), (0, 4)): 1, (4, (1, 0, 1, 0, 0, 4), (1, 3)): 1, (3, (1, 0, 1, 0, 0, 3), (2, 1)): 1, (3, (1, 0, 1, 1, 1, 3), (2, 1)): 1, (4, (1, 0, 1, 0, 0, 4), (2, 2)): 2, (4, (1, 0, 2, 1, 0, 2), (4, 0)): 1, (2, (1, 0, 1, 1, 1, 2), (1, 1)): 1, (3, (1, 0, 1, 1, 1, 3), (1, 2)): 1, (4, (1, 0, 1, 1, 1, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 2, 4), (1, 3)): 1, (3, (1, 0, 1, 0, 0, 3), (3, 0)): 1, (4, (1, 1, 2, 1, 0, 2), (0, 4)): 1, (2, (1, 0, 1, 0, 1, 2), (2, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (2, 2)): 2, (2, (1, 0, 1, 1, 1, 2), (2, 0)): 1, (4, (1, 0, 1, 0, 0, 4), (4, 0)): 1, (4, (1, 0, 1, 0, 1, 4), (2, 2)): 2, (4, (1, 0, 1, 0, 1, 4), (3, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (2, 2)): 1, (4, (1, 0, 1, 0, 2, 4), (3, 1)): 1, (2, (1, 0, 1, 0, 1, 2), (1, 1)): 1, (4, (1, 0, 1, 1, 2, 4), (0, 4)): 1, (3, (1, 0, 1, 0, 1, 3), (2, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (1, 3)): 1, (2, (1, 0, 1, 0, 0, 2), (0, 2)): 1, (4, (1, 0, 1, 2, 2, 4), (2, 2)): 2, (4, (1, 0, 2, 0, 0, 2), (4, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (3, 1)): 1, (3, (1, 0, 1, 0, 1, 3), (0, 3)): 1, (4, (1, 0, 1, 0, 1, 4), (1, 3)): 1, (2, (1, 0, 1, 0, 0, 2), (2, 0)): 1, (4, (1, 1, 2, 1, 0, 2), (4, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (0, 4)): 1, (4, (1, 0, 2, 0, 0, 2), (0, 4)): 1, (3, (1, 0, 1, 1, 1, 3), (3, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (1, 3)): 1, (4, (1, 1, 2, 1, 0, 2), (3, 1)): 1, (2, (1, 0, 1, 1, 1, 2), (0, 2)): 1, (4, (1, 0, 2, 0, 0, 2), (2, 2)): 2, (4, (1, 0, 1, 1, 1, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 1, 4), (0, 4)): 1, (4, (1, 0, 2, 1, 0, 2), (3, 1)): 1, (1, (1, 0, 1, 0, 0, 1), (1, 0)): 1, (3, (1, 0, 1, 1, 1, 3), (0, 3)): 1, (3, (1, 0, 1, 0, 1, 3), (3, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (4, 0)): 1, (1, (1, 0, 1, 0, 0, 1), (0, 1)): 1, (4, (1, 0, 2, 0, 0, 2), (3, 1)): 1, (4, (1, 0, 1, 0, 0, 4), (3, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (2, 2)): 2}
#         self.assertEquals(out,_distribute([1, 2, 3, 4], 'all', n = 100,dataformat= 'tests/enumeration/sc_1/cells.{}', seed=1010))

#     def testDistribute3(self):
#         from phenum.structures import _distribute
#         out = {(4, (1, 0, 1, 1, 1, 4), (2, 2)): 2, (4, (1, 0, 2, 1, 0, 2), (2, 2)): 3, (4, (1, 0, 1, 1, 1, 4), (0, 4)): 1, (3, (1, 0, 1, 0, 0, 3), (1, 2)): 1, (3, (1, 0, 1, 0, 1, 3), (1, 2)): 1, (4, (1, 0, 1, 0, 2, 4), (4, 0)): 1, (3, (1, 0, 1, 1, 1, 3), (3, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (3, 1)): 1, (4, (1, 0, 2, 1, 0, 2), (0, 4)): 1, (4, (1, 0, 2, 0, 0, 2), (1, 3)): 1, (4, (1, 0, 1, 1, 1, 4), (3, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (0, 4)): 1, (4, (1, 0, 2, 1, 0, 2), (1, 3)): 1, (4, (1, 0, 1, 0, 0, 4), (0, 4)): 1, (4, (1, 0, 1, 0, 0, 4), (1, 3)): 1, (3, (1, 0, 1, 0, 0, 3), (2, 1)): 1, (4, (1, 0, 1, 1, 2, 4), (4, 0)): 1, (4, (1, 0, 1, 0, 0, 4), (2, 2)): 2, (4, (1, 0, 2, 1, 0, 2), (4, 0)): 1, (3, (1, 0, 1, 1, 1, 3), (1, 2)): 1, (4, (1, 0, 1, 1, 1, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (1, 3)): 1, (3, (1, 0, 1, 1, 1, 3), (0, 3)): 1, (4, (1, 1, 2, 1, 0, 2), (0, 4)): 1, (3, (1, 0, 1, 0, 0, 3), (3, 0)): 1, (3, (1, 0, 1, 1, 1, 3), (2, 1)): 1, (4, (1, 0, 1, 1, 2, 4), (0, 4)): 1, (4, (1, 0, 1, 2, 2, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 0, 4), (4, 0)): 1, (4, (1, 0, 1, 0, 1, 4), (0, 4)): 1, (4, (1, 0, 1, 0, 1, 4), (3, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (2, 2)): 1, (4, (1, 0, 1, 0, 2, 4), (3, 1)): 1, (4, (1, 0, 1, 1, 2, 4), (2, 2)): 2, (3, (1, 0, 1, 0, 1, 3), (2, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (1, 3)): 1, (4, (1, 0, 1, 2, 2, 4), (2, 2)): 2, (4, (1, 0, 2, 0, 0, 2), (4, 0)): 1, (3, (1, 0, 1, 0, 1, 3), (0, 3)): 1, (4, (1, 0, 1, 0, 1, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 0, 4), (3, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (4, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (0, 4)): 1, (3, (1, 0, 1, 0, 0, 3), (0, 3)): 1, (4, (1, 0, 1, 2, 2, 4), (3, 1)): 1, (4, (1, 1, 2, 1, 0, 2), (3, 1)): 1, (4, (1, 0, 2, 0, 0, 2), (2, 2)): 2, (4, (1, 0, 1, 1, 1, 4), (1, 3)): 1, (4, (1, 0, 2, 1, 0, 2), (3, 1)): 1, (4, (1, 0, 2, 0, 0, 2), (0, 4)): 1, (4, (1, 0, 1, 0, 1, 4), (4, 0)): 1, (3, (1, 0, 1, 0, 1, 3), (3, 0)): 1, (4, (1, 0, 1, 2, 2, 4), (4, 0)): 1, (4, (1, 0, 1, 0, 2, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 1, 4), (2, 2)): 2, (4, (1, 0, 2, 0, 0, 2), (3, 1)): 1, (4, (1, 0, 1, 0, 2, 4), (2, 2)): 2}
#         self.assertEquals(out,_distribute([3, 4], 'all', n = 100,dataformat= 'tests/enumeration/sc_1/cells.{}', seed=1010))

#     def testDistribute4(self):
#         from phenum.structures import _distribute
#         out = {(4, (1, 0, 1, 0, 0, 4), (4, 0)): 1, (4, (1, 0, 1, 1, 2, 4), (0, 4)): 1, (4, (1, 0, 1, 1, 2, 4), (1, 3)): 1, (4, (1, 0, 1, 0, 0, 4), (1, 3)): 1, (4, (1, 0, 1, 1, 2, 4), (3, 1)): 1, (4, (1, 0, 1, 1, 2, 4), (2, 2)): 1, (4, (1, 0, 1, 0, 0, 4), (3, 1)): 2, (4, (1, 0, 1, 0, 0, 4), (2, 2)): 1, (4, (1, 0, 1, 1, 2, 4), (4, 0)): 1}
#         self.assertEquals(out,_distribute([1, 2, 3, 4], 'all',n=10,dataformat='tests/enumeration/sc_1/cells.{}', seed=1010, res_type='shape', res_values=[(1, 0, 1, 0, 0, 4), (1, 0, 1, 1, 2, 4)]))
        
# class TestDistribution(ut.TestCase):
#     """Tests of the _distribution subroutine."""

#     def testDistribution1_dataset(self):
#         from phenum.structures import _distribution

#         (f, dataset, gtotal) = _distribution('all', None, None, cast=float,cellsizes=[1, 2, 3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         dset_out = {1: {'gtotal': 2, 'stotals': {(1, 0, 1, 0, 0, 1): 2}, 'concs': [(0, 1), (1, 0)], 'ctotals': {(0, 1): 1, (1, 0): 1}, 'distr': {(1, 0, 1, 0, 0, 1): {(0, 1): 1, (1, 0): 1}}}, 2: {'gtotal': 9, 'stotals': {(1, 0, 1, 1, 1, 2): 3, (1, 0, 1, 0, 1, 2): 3, (1, 0, 1, 0, 0, 2): 3}, 'concs': [(0, 2), (1, 1), (2, 0)], 'ctotals': {(2, 0): 3, (0, 2): 3, (1, 1): 3}, 'distr': {(1, 0, 1, 1, 1, 2): {(2, 0): 1, (0, 2): 1, (1, 1): 1}, (1, 0, 1, 0, 1, 2): {(2, 0): 1, (0, 2): 1, (1, 1): 1}, (1, 0, 1, 0, 0, 2): {(2, 0): 1, (0, 2): 1, (1, 1): 1}}}, 3: {'gtotal': 12, 'stotals': {(1, 0, 1, 0, 0, 3): 4, (1, 0, 1, 0, 1, 3): 4, (1, 0, 1, 1, 1, 3): 4}, 'concs': [(0, 3), (1, 2), (2, 1), (3, 0)], 'ctotals': {(1, 2): 3, (3, 0): 3, (0, 3): 3, (2, 1): 3}, 'distr': {(1, 0, 1, 0, 0, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 0, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 1, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}}}, 4: {'gtotal': 54, 'stotals': {(1, 0, 1, 0, 1, 4): 6, (1, 0, 1, 1, 2, 4): 6, (1, 0, 1, 2, 2, 4): 6, (1, 0, 2, 0, 0, 2): 6, (1, 0, 1, 1, 1, 4): 6, (1, 1, 2, 1, 0, 2): 5, (1, 0, 2, 1, 0, 2): 7, (1, 0, 1, 0, 2, 4): 6, (1, 0, 1, 0, 0, 4): 6}, 'concs': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 'ctotals': {(4, 0): 9, (1, 3): 9, (3, 1): 9, (2, 2): 18, (0, 4): 9}, 'distr': {(1, 0, 1, 0, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 2, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 2, 0, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 1, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 1, (0, 4): 1}, (1, 0, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 3, (0, 4): 1}, (1, 0, 1, 0, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 0, 0, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}}}}
#         self.assertEquals(dset_out,dataset)
        
#     def testDistribution1_gtotal(self):
#         from phenum.structures import _distribution

#         (f, dataset, gtotal) = _distribution('all', None, None, cast=float,cellsizes=[1, 2, 3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         gtotal_out =  77
#         self.assertEquals(gtotal_out,gtotal)
        
#     def testDistribution2_dataset(self):
#         from phenum.structures import _distribution

#         (f, dataset, gtotal) = _distribution('all', None, None, cast=float,cellsizes=[3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         dset_out = {3: {'gtotal': 12, 'stotals': {(1, 0, 1, 0, 0, 3): 4, (1, 0, 1, 0, 1, 3): 4, (1, 0, 1, 1, 1, 3): 4}, 'concs': [(0, 3), (1, 2), (2, 1), (3, 0)], 'ctotals': {(1, 2): 3, (3, 0): 3, (0, 3): 3, (2, 1): 3}, 'distr': {(1, 0, 1, 0, 0, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 0, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 1, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}}}, 4: {'gtotal': 54, 'stotals': {(1, 0, 1, 0, 1, 4): 6, (1, 0, 1, 1, 2, 4): 6, (1, 0, 1, 2, 2, 4): 6, (1, 0, 2, 0, 0, 2): 6, (1, 0, 1, 1, 1, 4): 6, (1, 1, 2, 1, 0, 2): 5, (1, 0, 2, 1, 0, 2): 7, (1, 0, 1, 0, 2, 4): 6, (1, 0, 1, 0, 0, 4): 6}, 'concs': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 'ctotals': {(4, 0): 9, (1, 3): 9, (3, 1): 9, (2, 2): 18, (0, 4): 9}, 'distr': {(1, 0, 1, 0, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 2, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 2, 0, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 1, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 1, (0, 4): 1}, (1, 0, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 3, (0, 4): 1}, (1, 0, 1, 0, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 0, 0, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}}}}
#         self.assertEquals(dset_out,dataset)
        
#     def testDistribution2_gtotal(self):
#         from phenum.structures import _distribution

#         (f, dataset, gtotal) = _distribution('all', None, None, cast=float,cellsizes=[3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         gtotal_out =  66
#         self.assertEquals(gtotal_out,gtotal)
        
#     def testDistribution3_dataset(self):
#         from phenum.structures import _distribution

#         (f, dataset, gtotal) = _distribution('all', None, None,cast=float, cellsizes=[1, 2, 3, 4], dataformat='tests/enumeration/sc_1/cells.{}', res_type='shape', res_values=[(1, 0, 1, 0, 0, 4), (1, 0, 1, 1, 2, 4)])
#         dset_out = {1: {'gtotal': 0, 'stotals': {}, 'concs': [(0, 1), (1, 0)], 'ctotals': {(0, 1): 0, (1, 0): 0}, 'distr': {}}, 2: {'gtotal': 0, 'stotals': {}, 'concs': [(0, 2), (1, 1), (2, 0)], 'ctotals': {(2, 0): 0, (0, 2): 0, (1, 1): 0}, 'distr': {}}, 3: {'gtotal': 0, 'stotals': {}, 'concs': [(0, 3), (1, 2), (2, 1), (3, 0)], 'ctotals': {(1, 2): 0, (3, 0): 0, (0, 3): 0, (2, 1): 0}, 'distr': {}}, 4: {'gtotal': 12, 'stotals': {(1, 0, 1, 1, 2, 4): 6, (1, 0, 1, 0, 0, 4): 6}, 'concs': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 'ctotals': {(4, 0): 2, (1, 3): 2, (3, 1): 2, (2, 2): 4, (0, 4): 2}, 'distr': {(1, 0, 1, 1, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 0, 0, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}}}}
#         self.assertEquals(dset_out,dataset)
        
#     def testDistribution3_gtotal(self):
#         from phenum.structures import _distribution

#         (f, dataset, gtotal) = _distribution('all', None, None,cast=float, cellsizes=[1, 2, 3, 4], dataformat='tests/enumeration/sc_1/cells.{}', res_type='shape', res_values=[(1, 0, 1, 0, 0, 4), (1, 0, 1, 1, 2, 4)])
#         gtotal_out =  12
#         self.assertEquals(gtotal_out,gtotal)
        
# class TestDistributionSummmary(ut.TestCase):
#     """Tests of the _distribution_summary function."""

#     def testDistSum1_dset(self):
#         from phenum.structures import _distribution_summary

#         (dset,gt) = _distribution_summary([3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         dset_out = {3: {'gtotal': 12, 'stotals': {(1, 0, 1, 0, 0, 3): 4, (1, 0, 1, 0, 1, 3): 4, (1, 0, 1, 1, 1, 3): 4}, 'concs': [(0, 3), (1, 2), (2, 1), (3, 0)], 'ctotals': {(1, 2): 3, (3, 0): 3, (0, 3): 3, (2, 1): 3}, 'distr': {(1, 0, 1, 0, 0, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 0, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 1, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}}}, 4: {'gtotal': 54, 'stotals': {(1, 0, 1, 0, 1, 4): 6, (1, 0, 1, 1, 2, 4): 6, (1, 0, 1, 2, 2, 4): 6, (1, 0, 2, 0, 0, 2): 6, (1, 0, 1, 1, 1, 4): 6, (1, 1, 2, 1, 0, 2): 5, (1, 0, 2, 1, 0, 2): 7, (1, 0, 1, 0, 2, 4): 6, (1, 0, 1, 0, 0, 4): 6}, 'concs': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 'ctotals': {(4, 0): 9, (1, 3): 9, (3, 1): 9, (2, 2): 18, (0, 4): 9}, 'distr': {(1, 0, 1, 0, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 2, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 2, 0, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 1, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 1, (0, 4): 1}, (1, 0, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 3, (0, 4): 1}, (1, 0, 1, 0, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 0, 0, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}}}}
#         self.assertEqual(dset_out,dset)

#     def testDistSum1_gt(self):
#         from phenum.structures import _distribution_summary

#         (dset,gt) = _distribution_summary([3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         gt_out = 66
#         self.assertEqual(gt_out,gt)

#     def testDistSum2_dset(self):
#         from phenum.structures import _distribution_summary

#         (dset,gt) = _distribution_summary([1,2,3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         dset_out = {1: {'gtotal': 2, 'stotals': {(1, 0, 1, 0, 0, 1): 2}, 'concs': [(0, 1), (1, 0)], 'ctotals': {(0, 1): 1, (1, 0): 1}, 'distr': {(1, 0, 1, 0, 0, 1): {(0, 1): 1, (1, 0): 1}}}, 2: {'gtotal': 9, 'stotals': {(1, 0, 1, 1, 1, 2): 3, (1, 0, 1, 0, 1, 2): 3, (1, 0, 1, 0, 0, 2): 3}, 'concs': [(0, 2), (1, 1), (2, 0)], 'ctotals': {(2, 0): 3, (0, 2): 3, (1, 1): 3}, 'distr': {(1, 0, 1, 1, 1, 2): {(2, 0): 1, (0, 2): 1, (1, 1): 1}, (1, 0, 1, 0, 1, 2): {(2, 0): 1, (0, 2): 1, (1, 1): 1}, (1, 0, 1, 0, 0, 2): {(2, 0): 1, (0, 2): 1, (1, 1): 1}}}, 3: {'gtotal': 12, 'stotals': {(1, 0, 1, 0, 0, 3): 4, (1, 0, 1, 0, 1, 3): 4, (1, 0, 1, 1, 1, 3): 4}, 'concs': [(0, 3), (1, 2), (2, 1), (3, 0)], 'ctotals': {(1, 2): 3, (3, 0): 3, (0, 3): 3, (2, 1): 3}, 'distr': {(1, 0, 1, 0, 0, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 0, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}, (1, 0, 1, 1, 1, 3): {(1, 2): 1, (3, 0): 1, (0, 3): 1, (2, 1): 1}}}, 4: {'gtotal': 54, 'stotals': {(1, 0, 1, 0, 1, 4): 6, (1, 0, 1, 1, 2, 4): 6, (1, 0, 1, 2, 2, 4): 6, (1, 0, 2, 0, 0, 2): 6, (1, 0, 1, 1, 1, 4): 6, (1, 1, 2, 1, 0, 2): 5, (1, 0, 2, 1, 0, 2): 7, (1, 0, 1, 0, 2, 4): 6, (1, 0, 1, 0, 0, 4): 6}, 'concs': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 'ctotals': {(4, 0): 9, (1, 3): 9, (3, 1): 9, (2, 2): 18, (0, 4): 9}, 'distr': {(1, 0, 1, 0, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 2, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 2, 0, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 1, 1, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 1, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 1, (0, 4): 1}, (1, 0, 2, 1, 0, 2): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 3, (0, 4): 1}, (1, 0, 1, 0, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 0, 0, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}}}}
#         self.assertEqual(dset_out,dset)

#     def testDistSum2_gt(self):
#         from phenum.structures import _distribution_summary

#         (dset,gt) = _distribution_summary([1, 2, 3, 4], dataformat='tests/enumeration/sc_1/cells.{}')
#         gt_out = 77
#         self.assertEqual(gt_out,gt)

#     def testDistSum3_dset(self):
#         from phenum.structures import _distribution_summary

#         (dset,gt) = _distribution_summary([1,2,3, 4], HNFs=[(1, 0, 1, 0, 0, 4), (1, 0, 1, 1, 2, 4)],dataformat='tests/enumeration/sc_1/cells.{}')
#         dset_out = {1: {'gtotal': 0, 'stotals': {}, 'concs': [(0, 1), (1, 0)], 'ctotals': {(0, 1): 0, (1, 0): 0}, 'distr': {}}, 2: {'gtotal': 0, 'stotals': {}, 'concs': [(0, 2), (1, 1), (2, 0)], 'ctotals': {(2, 0): 0, (0, 2): 0, (1, 1): 0}, 'distr': {}}, 3: {'gtotal': 0, 'stotals': {}, 'concs': [(0, 3), (1, 2), (2, 1), (3, 0)], 'ctotals': {(1, 2): 0, (3, 0): 0, (0, 3): 0, (2, 1): 0}, 'distr': {}}, 4: {'gtotal': 12, 'stotals': {(1, 0, 1, 1, 2, 4): 6, (1, 0, 1, 0, 0, 4): 6}, 'concs': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 'ctotals': {(4, 0): 2, (1, 3): 2, (3, 1): 2, (2, 2): 4, (0, 4): 2}, 'distr': {(1, 0, 1, 1, 2, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}, (1, 0, 1, 0, 0, 4): {(4, 0): 1, (1, 3): 1, (3, 1): 1, (2, 2): 2, (0, 4): 1}}}}
#         self.assertEqual(dset_out,dset)

#     def testDistSum3_gt(self):
#         from phenum.structures import _distribution_summary

#         (dset,gt) = _distribution_summary([1,2,3, 4], HNFs=[(1, 0, 1, 0, 0, 4), (1, 0, 1, 1, 2, 4)],dataformat='tests/enumeration/sc_1/cells.{}')
#         gt_out = 12
#         self.assertEqual(gt_out,gt)
        
