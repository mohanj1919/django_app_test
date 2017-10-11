import React from 'react'
import { shallow, mount } from 'enzyme'
import expect, { createSpy, spyOn, isSpy } from 'expect'
import { 
        default as usersReducer } from '../../../../src/routes/Users/modules/users'

describe('Users login Reducer', () => {

    const initialState = {
         
    }

    it('Should be a function', () => {
        expect(usersReducer).toBeA('function');
    });

     it('should return the default state', () => {
        expect(usersReducer(undefined, {})).toEqual(initialState)
    })
})
