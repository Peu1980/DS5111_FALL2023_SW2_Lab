import pytest
import os
import sys
sys.path.append(".")

from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  1, "Test Fail for [1,1]"
    assert the_perceptron.predict([1,0]) ==  1, "Test Fail for [1,0]"
    assert the_perceptron.predict([0,1]) ==  1, "Test Fail for [0,1]"
    assert the_perceptron.predict([0,0]) ==  0, "Test Fail for [0,0]"


@pytest.mark.xfail(reason="Negative Test")
def test_fail_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,0]) ==  0, "Test Fail for [1,0]"
   

@pytest.mark.skipif(os.uname().sysname!='Linux', reason="Only suppoerted on Linux")
def test_os_perceptron():
    total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])

    assert total_memory >= 10, "Not enough total memory" 
    assert used_memory < 500, "Too much used memory"
    assert free_memory >=15, "Not enough free memory"


@pytest.mark.skip(reason="This test is not yet ready for prime time")
def test_skip_perceptron():
    my_test = True

    assert my_test == False, "This is always skipping"


@pytest.mark.parametrize(
        "trainingset, labels, expected",
        [
            ([[1,1],[1,0],[0,1],[0,0]],[1,1,1,0],[1,1,1,0]),
            ([[1,2],[2,3],[3,4],[4,5]],[1,1,1,1],[1,1,1,1]),
            ([[2,2],[3,3],[4,4],[5,5]],[1,1,1,1],[1,1,1,1]),
            ([[1,2],[1,3],[1,4],[1,5]],[0,1,1,1],[0,1,1,1]),
            ([[2,1],[3,2],[4,3],[5,4]],[1,1,0,0],[1,1,0,0]),
            ([[1,5],[1,3],[3,5],[2,5]],[1,1,0,1],[1,1,0,1])
         ]
        )
def test_para_perceptron(trainingset, labels, expected):
    para_perceptron = Perceptron()
    para_perceptron.train(trainingset, labels)

    para_predicted = []
    for para_input in trainingset:
        para_predicted.append(para_perceptron.predict(para_input))

    assert para_predicted == expected, "Predictions are not maching with expected values"


## EXTRA CREDIT
@pytest.fixture
def test_fixture(trainingset = [[1,1],[1,0],[0,1],[0,0]],labels = [1,1,1,0]):
    para_perceptron_extra = Perceptron()
    para_perceptron_extra.train(trainingset, labels)
    
    return para_perceptron_extra


@pytest.mark.parametrize(
        "testingset, labels",
        [
            ([[1,1],[1,0],[0,1],[0,0]],[1,1,1,0]),
            ([[1,2],[2,3],[3,4],[4,5]],[1,1,1,1]),
            ([[2,2],[3,3],[4,4],[5,5]],[1,1,1,1]),
            ([[1,2],[1,3],[1,4],[1,5]],[0,1,1,1]),
            ([[2,1],[3,2],[4,3],[5,4]],[1,1,0,0]),
            ([[1,5],[1,3],[3,5],[2,5]],[1,1,0,1])
         ],
         indirect=["testingset"])
def test_para_perceptron_extra(test_fixture,testingset,labels):
    para_predicted = []
    for para_input in testingset:
        para_predicted.append(para_perceptron_extra.predict(para_input))

    assert para_predicted == labels, "Predictions are not maching with expected values"

