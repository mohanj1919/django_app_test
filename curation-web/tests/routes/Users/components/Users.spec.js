import React from 'react'
import CohortsLayout from '../../../../src/routes/Users/components/Users'
import expect from 'expect'
import { mount } from 'enzyme';
describe('Users Component', () => {
    beforeEach(function () {
        localStorage.logged_user_role = 'admin'
    });
    let wrapper = mount(<CohortsLayout/>);
    describe('should render children', () => {
        it('should get container, so that it is rendering children(profile)', () => {
            expect(wrapper.find('.container')).toExist
            expect(wrapper.find('.cohort-configure')).toExist
        })
    })
})