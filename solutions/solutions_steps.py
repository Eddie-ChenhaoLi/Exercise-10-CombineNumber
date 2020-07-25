from behave import *
from demo import *
import json


@Given('I have a list of positive integers {l}')
def step_impl(context, l):
    list = json.loads(l)
    context.list = list


@When('the list is sorted from largest to smallest {sort}')
def step_impl(context, sort):
    context.sort = sort_list(context.list)
    assert context.sort == json.loads(sort)


@When('the sorted list is converted to a string {s}')
def step_impl(context, s):
    context.s = list_string(context.sort)
    assert context.s == s


@Then('I should convert the string to a integer {i:d}')
def step_impl(context, i):
    context.i = string_int(context.s)
    assert context.i == i
