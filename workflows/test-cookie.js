const JuejinHelper = require("juejin-helper");
const env = require("./utils/env");

async function testCookie() {
  const cookie = env.COOKIE;
  
  if (!cookie) {
    console.error("错误: 未找到 COOKIE 配置");
    return;
  }
  
  console.log("开始测试 Cookie...\n");
  console.log("Cookie 长度:", cookie.length);
  console.log("Cookie 前100字符:", cookie.substring(0, 100) + "...\n");
  
  // 检查必要的字段
  const checks = {
    'sessionid': cookie.includes('sessionid='),
    'sessionid_ss': cookie.includes('sessionid_ss='),
    '__tea_cookie_tokens': cookie.includes('__tea_cookie_tokens'),
    'sid_tt': cookie.includes('sid_tt='),
    'uid_tt': cookie.includes('uid_tt=')
  };
  
  console.log("Cookie 字段检查:");
  Object.entries(checks).forEach(([field, exists]) => {
    console.log(`  ${field}: ${exists ? '✓' : '✗'}`);
  });
  console.log();
  
  // 尝试解析 __tea_cookie_tokens
  try {
    const tokensMatch = cookie.match(/__tea_cookie_tokens_\d+=([^;]+)/);
    if (tokensMatch) {
      const encodedValue = tokensMatch[1];
      const decodedOnce = decodeURIComponent(encodedValue);
      const decodedTwice = decodeURIComponent(decodedOnce);
      const tokens = JSON.parse(decodedTwice);
      console.log("✓ __tea_cookie_tokens 解析成功:");
      console.log("  web_id:", tokens.web_id);
      console.log("  user_unique_id:", tokens.user_unique_id);
      console.log("  timestamp:", new Date(tokens.timestamp).toLocaleString());
      console.log();
    } else {
      console.warn("⚠ 未找到 __tea_cookie_tokens 字段\n");
    }
  } catch (e) {
    console.error("✗ __tea_cookie_tokens 解析失败:", e.message);
    console.log();
  }
  
  // 尝试登录
  console.log("尝试登录...");
  const juejin = new JuejinHelper();
  try {
    await juejin.login(cookie);
    const user = juejin.getUser();
    console.log("✓ 登录成功!");
    console.log("  用户名:", user.user_name);
    console.log("  用户ID:", user.user_id);
  } catch (e) {
    console.error("✗ 登录失败:", e.message);
    console.error("\n可能的原因:");
    console.error("1. Cookie 已过期（最常见）");
    console.error("2. Cookie 格式不正确");
    console.error("3. Cookie 缺少必要的字段");
    console.error("\n解决方案:");
    console.error("请访问 https://juejin.cn 重新获取 Cookie");
  }
}

testCookie().catch(console.error);

