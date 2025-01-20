const env = process.env || {};

module.exports = {
  /* 掘金Cookie */
  // COOKIE: env.COOKIE,
    COOKIE: "__tea_cookie_tokens_2608=%7B%22web_id%22%3A%227435802743686596096%22%2C%22user_unique_id%22%3A%227435802743686596096%22%2C%22timestamp%22%3A1731282775939%7D; n_mh=tzO9uUFHV3SORYqaaDIX3-5k3wt2U651nnC_0LtXeDg; sid_guard=527d990289c9f3c56261f67947e39f54|1731282802|31536000|Mon,+10-Nov-2025+23:53:22+GMT; uid_tt=33f0a8e220a818991536ede6490929dc; uid_tt_ss=33f0a8e220a818991536ede6490929dc; sid_tt=527d990289c9f3c56261f67947e39f54; sessionid=527d990289c9f3c56261f67947e39f54; sessionid_ss=527d990289c9f3c56261f67947e39f54; is_staff_user=false; sid_ucp_v1=1.0.0-KDdmNDAzZDBlNWE4OGJkNTAzNjlhNzQ3MWNkY2JiNGE3MWQ3MjBlNTQKFgjorMC-_fXBBxDyjsW5BhiwFDgIQDgaAmxxIiA1MjdkOTkwMjg5YzlmM2M1NjI2MWY2Nzk0N2UzOWY1NA; ssid_ucp_v1=1.0.0-KDdmNDAzZDBlNWE4OGJkNTAzNjlhNzQ3MWNkY2JiNGE3MWQ3MjBlNTQKFgjorMC-_fXBBxDyjsW5BhiwFDgIQDgaAmxxIiA1MjdkOTkwMjg5YzlmM2M1NjI2MWY2Nzk0N2UzOWY1NA; store-region=cn-fj; store-region-src=uid; _ga=GA1.2.1234608364.1731282805; _ga_S695FMNGPJ=GS1.2.1731282805.1.0.1731282805.60.0.0; _jj_ext=1; _tea_utm_cache_2018={\"utm_source\":\"gold_browser_extension\"}; _tea_utm_cache_2608={\"utm_source\":\"gold_browser_extension\"}; MONITOR_WEB_ID=ef884819-75bd-42e8-be12-8ccef7f5c3dd; MONITOR_DEVICE_ID=3080490b-7569-446c-b676-2c7c82966f51; s_v_web_id=verify_m5ucy2q8_uyOhdUKy_aD56_4ako_8nqv_FeDyEEBNdKrI",

  /* 多用户掘金Cookie, 当有1名以上用户时填写, 支持同时最多可配置5名用户 */
  COOKIE_2: env.COOKIE_2,
  COOKIE_3: env.COOKIE_3,
  COOKIE_4: env.COOKIE_4,
  COOKIE_5: env.COOKIE_5,
  /**
   * 邮箱配置
   * user 发件人邮箱, pass, 发件人密码, to收件人
   */
  EMAIL_USER: env.EMAIL_USER,
  EMAIL_PASS: env.EMAIL_PASS,
  EMAIL_TO: env.EMAIL_TO,
  /**
   * 钉钉配置
   * https://open.dingtalk.com/document/robots/custom-robot-access
   */
  DINGDING_WEBHOOK: env.DINGDING_WEBHOOK,
  /**
   * PushPlus配置
   * http://www.pushplus.plus/doc/guide/openApi.html
   */
  PUSHPLUS_TOKEN: env.PUSHPLUS_TOKEN,
  /**
   * 企业微信机器人配置
   * https://developer.work.weixin.qq.com/document/path/91770
   */
  WEIXIN_WEBHOOK: env.WEIXIN_WEBHOOK,
  /**
   * server酱推送key
   * https://sct.ftqq.com/sendkey
   */
  SERVERPUSHKEY: env.SERVERPUSHKEY,
  /**
   * 飞书配置
   */
  FEISHU_WEBHOOK: env.FEISHU_WEBHOOK
};
