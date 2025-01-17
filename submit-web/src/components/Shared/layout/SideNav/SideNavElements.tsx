export const Routes: RouteType[] = [
  {
    name: "Root",
    path: "/",
  },
  {
    name: "About",
    path: "/aboutpage",
  },
  {
    name: "Lazy Loaded Page",
    path: "/newpage",
  },
  {
    name: "Plans",
    path: "/eao-plans",
  },
  {
    name: "Users",
    path: "/users",
  },
];

export const AuthenticatedRoutes: RouteType[] = [
  {
    name: "Profile",
    path: "/profile",
  },
];

export interface RouteType {
  name: string;
  path: string;
  group?: string;
  routes?: RouteType[];
}
