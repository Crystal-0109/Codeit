import { BrowserRouter, Route, Routes } from "react-router-dom";
import App from "./components/App";
import HomePage from "./pages/HomePage";
import CoursePage from "./pages/CoursePage";
import CourseListPage from "./pages/CourseListPage";
import QuestionPage from "./pages/QuestionPage";
import QuestionListPage from "./pages/QuestionListPage";
import WishlistPage from "./pages/WishlistPage";

function Main() {
  return (
    <BrowserRouter>
      <App>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="courses">
            <Route index element={<CourseListPage />} />
            <Route path="react-frontend-development" element={<CoursePage />} />
          </Route>
          <Route path="questions" element={<QuestionListPage />} />
          <Route path="questions/616825" element={<QuestionPage />} />
          <Route path="wishlist" element={<WishlistPage />} />
        </Routes>
      </App>
    </BrowserRouter>
  );
}

export default Main;
