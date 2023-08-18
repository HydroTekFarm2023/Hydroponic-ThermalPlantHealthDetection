import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ApiDataPage } from './api-data.page';

describe('ApiDataPage', () => {
  let component: ApiDataPage;
  let fixture: ComponentFixture<ApiDataPage>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(ApiDataPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
