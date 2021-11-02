from challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import *


def test_enqueue():
    expected='miky'
    miky = Dog('miky')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(miky)
    actual=animalShelter.front.name
    assert actual==expected

def test_enqueue_with_multiple_animals():
    expected='kitty'
    miky = Dog('miky')
    boby=Dog('boby')
    kitty=Cat('kitty')
    mshmsh=Cat('mshmsh')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(kitty)
    animalShelter.enqueue(miky)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(mshmsh)

    actual=animalShelter.front.name
    assert actual==expected

def test_dequeue():
    expected='miky'
    miky = Dog('miky')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(miky)
    actual=animalShelter.dequeue('dog')

    assert actual==expected

def test_dequeue_if_no_animal_in_shelter():
    expected=None
    animalShelter=AnimalShelter()
    actual=animalShelter.dequeue('dog')

    assert actual==expected

def test_denqueue_with_multiple_animals():
    expected='kitty'

    miky = Dog('miky')
    boby=Dog('boby')
    kitty=Cat('kitty')
    mshmsh=Cat('mshmsh')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(miky)
    animalShelter.enqueue(kitty)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(mshmsh)

    actual=animalShelter.dequeue('cat')

    assert actual==expected
